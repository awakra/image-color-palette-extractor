import os
from app import create_app

# Determine the configuration to use (e.g., from an environment variable)
# Defaults to 'development' if FLASK_CONFIG is not set
config_name = os.getenv('FLASK_CONFIG', 'development')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', True), host='0.0.0.0', port=int(os.getenv('PORT', 5000)))