from flask import Blueprint

# Create a Blueprint object
palette_bp = Blueprint('palette', __name__, template_folder='templates')

# Import routes at the end to avoid circular dependencies
from . import routes