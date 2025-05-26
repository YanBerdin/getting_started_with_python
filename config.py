import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
# # This code generates a random secret key for use in a Flask application (ex. generate cookies).
# or
# http://www.miniwebtool.com/django-secret-key-generator/ 

# Récupération des variables d'environnement
SECRET_KEY = os.environ.get("SECRET_KEY")
FB_APP_ID = int(os.environ.get("FB_APP_ID", 0))

#? Explication du code de génération de clé secrète

# config.py présente une méthode pour générer une clé secrète aléatoire, élément essentiel pour une application Flask.

# Le code expliqué fonctionne ainsi :

# 1. Il importe deux modules Python standard : `random` (pour la génération de nombres aléatoires) et `string` (qui contient des constantes de chaînes de caractères).

# 2. Ensuite, il utilise une liste en compréhension pour :
#    - Sélectionner 24 caractères aléatoires depuis `string.printable` (qui contient tous les caractères ASCII imprimables)
#    - Joindre ces caractères en une seule chaîne avec la méthode `join()`

# Cette clé secrète est cruciale pour la sécurité d'une application Flask,  => sert à signer les cookies de session et à protéger contre les attaques CSRF (Cross-Site Request Forgery)..

# Configuration de la base de données
# Vérifier si on doit utiliser SQLite au lieu de MySQL
USE_SQLITE = os.environ.get("USE_SQLITE", "false").lower() == "true"

if USE_SQLITE:
    # Configuration SQLite
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    # Configuration MySQL
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "fbapp_db")
    
    # URI de connexion MySQL avec PyMySQL
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

# Option pour désactiver les signaux de modification (recommandé pour les performances)
SQLALCHEMY_TRACK_MODIFICATIONS = False
