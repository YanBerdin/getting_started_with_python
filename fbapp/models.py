from flask_sqlalchemy import SQLAlchemy
import logging as lg

import enum

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

# Create database connection object
db = SQLAlchemy()

class Content(db.Model):
    #L'appel à db.Column crée une nouvelle colonne dans la table
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    # La méthode __init__ construit l'instance
    # elle est appelée lors de la création d'un nouvel objet Content.
    def __init__(self, description, gender):
        self.description = description
        self.gender = gender
    # Content is a model representing a piece of content in the database.



def init_db():
    db.drop_all()
    db.create_all()
    # db.session.add(Content("THIS IS SPARTAAAAAAA!!!", 1))
    # db.session.add(Content("What's your favorite scary movie?", 0))
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", Gender['male']))
    db.session.add(Content("What's your favorite scary movie?", Gender['female']))
    db.session.add(Content('Personne ne te faisait pitié, ni sur le moment, ni après, on était absolument sans défense devant toi.', Gender['male']))
    db.session.commit()
    lg.warning('Database initialized!')
