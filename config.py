import os

class Config:
    """Base configuration class. Contains default configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    # Add other production-specific configurations here
    # For example, database URI from environment variable
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Dictionary to access config classes by name
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}