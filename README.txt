# Nightshift Tools Project

## Overview
Nightshift Tools is a web application built with Flask for managing and displaying Excel files. It allows users to upload Excel files, view a list of uploaded files, and display specific sheets with tabular data.

## Features
- **File Upload**: Upload Excel files (.xlsx) for analysis.
- **View Uploads**: List of uploaded files by upload date.
- **Display Sheet**: View specific sheets from uploaded Excel files.

## Project Structure

```plaintext
/nightshift-tools
|-- app.py               # Main Flask application file
|-- static/              # Static files (CSS, JS, images)
|   |-- css/
|   |   |-- bootstrap.min.css
|   |-- js/
|   |   |-- bootstrap.bundle.min.js
|   |-- images/
|       |-- city-flat.jpg
|-- templates/           # HTML templates
|   |-- display_sheet.html
|   |-- index.html
|   |-- upload.html
|   |-- view_uploads.html
|-- uploads/             # Directory for storing uploaded files
|-- README.txt           # Project documentation

# Installation

1. Clone the repository: `git clone https://github.com/NsChadmin/Nightshift-Tools-Project.git`
2. Navigate to the project directory: `cd nightshift-tools`
3. Install dependencies: `pip install -r requirements.txt`

# Usage

1. Run the Flask application: `python app.py`
2. Open your web browser and go to [http://localhost:8000/](http://localhost:8000/)

# Dependencies

- Flask: `pip install flask`
- pandas: `pip install pandas`
- numpy: `pip install numpy`
- Bootstrap 5.3: Included in the static files

# Contributing

If you find any issues or have suggestions for improvement, feel free to create an issue or submit a pull request.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
