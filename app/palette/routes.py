from flask import render_template, request, redirect, url_for, flash, current_app
from . import palette_bp 
import datetime
from werkzeug.utils import secure_filename
import os
from app.utils.color_processing import extract_palette 

UPLOAD_FOLDER_NAME = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """
    Checks if the file has an allowed extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@palette_bp.route('/')
def index():
    """
    Serves the main page of the palette extractor.
    Passes the current year to the template for the footer.
    """
    return render_template('index.html', title='Image Color Palette Extractor')

@palette_bp.route('/upload', methods=['POST']) 
def upload_image(): 
    """
    Handles image upload and redirects to the results page.
    """
    if 'image' not in request.files:
        flash('No file part')
        return redirect(url_for('palette.index'))

    file = request.files['image']

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('palette.index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        upload_dir_path = os.path.join(current_app.static_folder, UPLOAD_FOLDER_NAME)

        os.makedirs(upload_dir_path, exist_ok=True) 

        filepath = os.path.join(upload_dir_path, filename)
        file.save(filepath)

        image_static_path = f'{UPLOAD_FOLDER_NAME}/{filename}'

        try:
            palette = extract_palette(filepath, num_colors=10)
            return render_template('results.html',
                                   palette=palette,
                                   image_url=url_for('static', filename=image_static_path),
                                   year=datetime.datetime.now().year,
                                   title="Palette Results")
        except Exception as e:
            flash(f'Error processing image: {e}')
            return redirect(url_for('palette.index'))

    else:
        flash('Invalid file type. Allowed types are: png, jpg, jpeg, gif')
        return redirect(url_for('palette.index'))