from flask import Flask
from .views import app
# Initialize the Flask application

from . import models

# Connect sqlalchemy to app
models.db.init_app(app)

@app.cli.command()
def init_db():
    models.init_db()
    """Initialize the database."""
    print("Database initialized.")