from src.app import app

__author__ = 'Alessandro Bresciani'

app.run(debug=app.config['DEBUG'], port=4990)