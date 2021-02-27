# Importing the Flask dependency
from flask import Flask

# Creating a new flask app instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


