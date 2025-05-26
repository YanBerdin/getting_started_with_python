from flask import Flask
import sys, os
from flask import Flask, render_template # Import Flask and render_template for rendering HTML templates

# Ajoutez le répertoire parent au path pour importer config
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
@app.route('/index/')
def index():
    # return "Hello world !"
    return render_template('index.html')

if __name__ == "__main__":
    app.run()


