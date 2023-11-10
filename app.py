import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pandas as pd
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Set the path where uploaded files will be stored

# Error handling for creating the 'uploads' directory
try:
    os.makedirs('uploads', exist_ok=True)
except OSError:
    print("Error creating the 'uploads' directory")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(file_path)
            return redirect(url_for('display_sheet', uploaded_file_path=file_path))
    
    return render_template('index.html')

@app.route('/uploads', methods=['GET'])
def list_uploaded_files():
    uploaded_files = []
    uploads_dir = os.path.join(app.static_folder, 'uploads')
    for filename in os.listdir(uploads_dir):
        if filename.endswith('.xlsx'):
            uploaded_files.append(filename)
    return render_template('uploads.html', uploaded_files=uploaded_files)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/display_sheet', methods=['GET', 'POST'])
def display_sheet():
    uploaded_file_path = request.form.get('uploaded_file_path')
    selected_sheet = request.form.get('selected_sheet')
    
    if uploaded_file_path and selected_sheet:
        try:
            # Load the selected sheet
            df = pd.read_excel(uploaded_file_path, sheet_name=selected_sheet)
            
            # Find the row containing "Time Period"
            time_period_row = df[df['CARS'] == 'Time Period'].index[0]
            
            # Extract the header and data rows
            header_row = df.columns.tolist()
            data_rows = df.iloc[time_period_row+1:].fillna(0)
            
            # Build the table HTML
            table_html = '<table class="table table-bordered"><thead><tr>'
            for header in header_row:
                table_html += f'<th>{header}</th>'
            table_html += '</tr></thead><tbody>'
            
            for _, row in data_rows.iterrows():
                table_html += '<tr>'
                for value in row.tolist():
                    table_html += f'<td>{value}</td>'
                table_html += '</tr>'
                
            table_html += '</tbody></table>'
            
            return render_template('display_sheet.html', table_html=table_html, uploaded_file_path=uploaded_file_path, selected_sheet=selected_sheet)
        
        except Exception as e:
            error_message = "Error: Invalid format."
            return render_template('display_sheet.html', error_message=error_message)
    
    return render_template('display_sheet.html')

@app.route('/view_uploads', methods=['GET'])
def view_uploads():
    uploads_dir = os.path.join(app.static_folder, 'uploads')
    files_by_date = {}

    # Iterate through the files in the uploads directory
    for filename in os.listdir(uploads_dir):
        file_path = os.path.join(uploads_dir, filename)
        if os.path.isfile(file_path):
            timestamp = os.path.getmtime(file_path)
            upload_date = datetime.fromtimestamp(timestamp)
            date_str = upload_date.strftime('%B %d')

            if date_str not in files_by_date:
                files_by_date[date_str] = []
            files_by_date[date_str].append(filename)

    return render_template('view_uploads.html', files_by_date=files_by_date)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
