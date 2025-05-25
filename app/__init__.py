# /image-color-palette-extractor/app/__init__.py

from flask import Flask
from config import app_config # Import the configuration dictionary
import datetime # Import datetime

def create_app(config_name='default'):
    """
    Application factory function.
    Creates and configures the Flask application instance.

    Args:
        config_name (str): The name of the configuration to use (e.g., 'development', 'production').

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration from config.py based on config_name
    current_config = app_config.get(config_name, app_config['default'])
    app.config.from_object(current_config)

    # Register context processor to make 'year' available in all templates
    @app.context_processor
    def inject_current_year():
        """Injects the current year into the template context."""
        return {'year': datetime.datetime.now().year}

    # Initialize Flask extensions here if any (e.g., db, login_manager)

    # Register Blueprints
    from .palette import palette_bp as palette_blueprint
    app.register_blueprint(palette_blueprint)
    # If your blueprint had a url_prefix, e.g., url_prefix='/palette',
    # then routes in that blueprint would be accessible under /palette/
    # app.register_blueprint(palette_blueprint, url_prefix='/palette')

    return app