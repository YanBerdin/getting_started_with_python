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

# Cette clé secrète est cruciale pour la sécurité d'une application Flask, car elle sert à signer les cookies de session et à protéger contre les attaques CSRF (Cross-Site Request Forgery). Une clé forte et aléatoire comme celle générée par ce code améliore significativement la sécurité de l'application.
