from flask import Flask
import sys, os

# Ajoutez le répertoire parent au path pour importer config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return "Hello world !"

if __name__ == "__main__":
    app.run()
# This is a simple Flask application that returns "Hello world !" when accessed at the root URL.
# To run this application, save it as views.py and execute it with Python.
# Make sure you have Flask installed in your Python environment.
# You can install Flask using pip:
# pip install Flask
# To run the application, use the command:
# python views.py
# Ensure that the Flask application is running by executing this script.
# You can then access the application in your web browser at http://