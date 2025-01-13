from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the app, __name__ is the name of the current module which is currently main.py
app = Flask(__name__)

# Create Database

# Create Routes
@app.route('/')
def home():
    return {'message': 'Hello World'}

# remove before production as this is for debugging and development
# refreshs for you so you can just reload the web page and not restart the server
if __name__ == '__main__':
    app.run(debug=True)
