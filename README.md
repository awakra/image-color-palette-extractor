# Image Color Palette Extractor

A Flask-based web application that allows users to upload an image and extract its dominant color palette. The application displays the top colors visually and provides their HEX and RGB codes.

## Features

- **Image Upload:** Users can upload images in common formats (PNG, JPG, JPEG, GIF).
- **Color Palette Extraction:**
  - Dominant colors are extracted using Pillow (PIL Fork) library's quantization methods.
  - Intelligent fallback mechanism for quantization (`libimagequant` -> `mediancut` -> default).
  - Displays a configurable number of top colors (default is 10).
- **Visual Palette Display:**
  - Extracted colors are shown as interactive color boxes.
  - The background of each box is set to the actual color.
  - The HEX code is displayed on each color box.
- **Interactive Color Codes:**
  - Clicking on a color box copies its HEX code to the clipboard.
  - A tabbed interface allows users to view the full list of extracted color codes in both:
    - HEX format (e.g., `#RRGGBB`)
    - RGB format (e.g., `rgb(R, G, B)`)
- **User-Friendly Interface:**
  - Clean and modern design.
  - Responsive layout for different screen sizes.
  - Flash messages for user feedback (e.g., successful upload, errors).
- **Dynamic Content:** The current year in the footer is updated automatically.

## Tech Stack

- **Backend:** Python, Flask
  - Flask Blueprints for modular application structure.
  - Werkzeug for WSGI and utility functions (e.g., `secure_filename`).
- **Image Processing:** Pillow 
- **Frontend:** HTML, CSS, JavaScript (vanilla)
  - Jinja2 for templating.
- **Development Environment:** Virtual Environment (`venv`)

## Project Structure

```
image-color-palette-extractor/
├── app/                    # Main application package
│   ├── __init__.py         # Application factory
│   ├── palette/            # Blueprint for palette extraction features
│   │   ├── __init__.py     # Blueprint initialization
│   │   ├── routes.py       # Routes for the palette blueprint
│   │   └── templates/      # Templates specific to the palette blueprint (deprecated, moved to app/templates)
│   ├── static/             # Static files (CSS, JS, uploaded images)
│   │   ├── css/
│   │   │   └── style.css
│   │   └── uploads/        # Directory for user-uploaded images (created dynamically)
│   ├── templates/          # Global application templates
│   │   ├── base.html       # Base template for all pages
│   │   ├── index.html      # Homepage with upload form
│   │   └── results.html    # Page to display extracted palette
│   └── utils/              # Utility modules
│       └── color_processing.py # Logic for color extraction
├── venv/                   # Virtual environment directory (typically in .gitignore)
├── config.py               # Configuration settings for the application
├── requirements.txt        # Python package dependencies
├── run.py                  # Script to run the Flask development server
└── README.md               # This file
```

## Setup and Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository (if applicable)

If you were cloning this from a remote repository (like GitHub):

```bash
git clone https://github.com/awakra/image-color-palette-extractor
cd image-color-palette-extractor
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment (e.g., named 'venv')
python -m venv venv

# Activate the virtual environment
# On Windows (Git Bash or MINGW64):
source venv/Scripts/activate
# On Windows (Command Prompt or PowerShell):
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

### 3. Install Dependencies

Install all the required Python packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Use the `run.py` script or the Flask CLI to start the development server.

```bash
flask run
```

Or, if `FLASK_APP` is not automatically detected (though `run.py` should handle this if it imports `create_app` from `app`):

```bash
export FLASK_APP=run.py  # For macOS/Linux
# set FLASK_APP=run.py    # For Windows Command Prompt
# $env:FLASK_APP="run.py" # For Windows PowerShell
flask run
```

The application should now be running, typically at `http://127.0.0.1:5000/`.

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. You will see the image upload form. Click "Choose File" to select an image from your computer.
3. Click the "Upload Image & Extract Palette" button.
4. If the upload and processing are successful, you will be redirected to the results page.
5. On the results page:
   - View the uploaded image.
   - See the visual palette of dominant colors. Click any color box to copy its HEX code.
   - Use the tabs to switch between viewing the color codes in HEX or RGB format.
6. Click "Upload Another Image" to return to the homepage and process a new image.
