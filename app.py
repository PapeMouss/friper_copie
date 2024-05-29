# app.py

from flask import Flask
from flask_login import LoginManager
from database import engine

# Créez une instance de l'application Flask
app = Flask(__name__)

# Importez vos routes Flask depuis routes.py
from routes import *

# Point d'entrée de l'application Flask
if __name__ == '__main__':
    print("L'application Flask démarre...")
    app.run(debug=True)

####
# app.py
app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # Clé secrète pour sécuriser les sessions utilisateur

# Configurez Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Configurez le moteur de session SQLAlchemy pour Flask-Login
@login_manager.user_loader
def load_user(user_id):
    from models import Utilisateur  # Importez votre modèle Utilisateur ici
    Session = sessionmaker(bind=engine)
    session = Session()
    return session.query(Utilisateur).get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    # Redirigez l'utilisateur non authentifié vers la page de connexion
    return 'Unauthorized', 401

# Importez vos routes Flask depuis routes.py
from routes import *

# Point d'entrée de l'application Flask
if __name__ == '__main__':
    print("L'application Flask démarre...")
    app.run(debug=True)
