# routes.py

from flask import jsonify, request
from sqlalchemy.orm import sessionmaker

from app import app
from models import Utilisateur, Produit  # Importez vos modèles de données SQLAlchemy

# Importez votre session SQLAlchemy depuis database.py
from database import Session

# Routes pour les utilisateurs

@app.route('/utilisateurs', methods=['GET'])
def get_utilisateurs():
    session = Session()
    utilisateurs = session.query(Utilisateur).all()
    session.close()
    return jsonify([utilisateur.serialize() for utilisateur in utilisateurs])

@app.route('/utilisateurs/<int:utilisateur_id>', methods=['GET'])
def get_utilisateur(utilisateur_id):
    session = Session()
    utilisateur = session.query(Utilisateur).get(utilisateur_id)
    session.close()
    if utilisateur:
        return jsonify(utilisateur.serialize()), 200
    else:
        return jsonify({'message': 'Utilisateur non trouvé'}), 404

# Ajoutez d'autres routes pour les produits, les commandes, etc.

@app.route('/utilisateurs', methods=['POST'])
def create_utilisateur():
    data = request.json
    nouvel_utilisateur = Utilisateur(nom=data['nom'], email=data['email'])
    session = Session()
    session.add(nouvel_utilisateur)
    session.commit()
    session.close()
    return jsonify(nouvel_utilisateur.serialize()), 201

# Ajoutez des routes pour la mise à jour et la suppression des utilisateurs

# Routes pour les produits

@app.route('/produits', methods=['POST'])
def create_produit():
    data = request.json
    nouveau_produit = Produit(nom=data['nom'], description=data['description'], prix=data['prix'], marque_id=data['marque_id'])
    session = Session()
    session.add(nouveau_produit)
    session.commit()
    session.close()
    return jsonify(nouveau_produit.serialize()), 201

@app.route('/produits/<int:produit_id>', methods=['PUT'])
def update_produit(produit_id):
    session = Session()
    produit = session.query(Produit).get(produit_id)
    if not produit:
        session.close()
        return jsonify({'message': 'Produit non trouvé'}), 404

    data = request.json
    produit.nom = data.get('nom', produit.nom)
    produit.description = data.get('description', produit.description)
    produit.prix = data.get('prix', produit.prix)
    produit.marque_id = data.get('marque_id', produit.marque_id)
    session.commit()
    session.close()
    return jsonify(produit.serialize()), 200

@app.route('/produits/<int:produit_id>', methods=['DELETE'])
def delete_produit(produit_id):
    session = Session()
    produit = session.query(Produit).get(produit_id)
    if not produit:
        session.close()
        return jsonify({'message': 'Produit non trouvé'}), 404

    session.delete(produit)
    session.commit()
    session.close()
    return jsonify({'message': 'Produit supprimé'}), 200
#####


# Routes pour les produits

@app.route('/produits', methods=['GET'])
def get_produits():
    session = Session()
    produits = session.query(Produit).all()
    session.close()
    return jsonify([produit.serialize() for produit in produits])

@app.route('/produits/<int:produit_id>', methods=['GET'])
def get_produit(produit_id):
    session = Session()
    produit = session.query(Produit).get(produit_id)
    session.close()
    if produit:
        return jsonify(produit.serialize()), 200
    else:
        return jsonify({'message': 'Produit non trouvé'}), 404

# Ajoutez des routes pour la création, la mise à jour et la suppression des produits

# Routes pour les commandes

@app.route('/commandes', methods=['GET'])
def get_commandes():
    session = Session()
    commandes = session.query(Commande).all()
    session.close()
    return jsonify([commande.serialize() for commande in commandes])

@app.route('/commandes/<int:commande_id>', methods=['GET'])
def get_commande(commande_id):
    session = Session()
    commande = session.query(Commande).get(commande_id)
    session.close()
    if commande:
        return jsonify(commande.serialize()), 200
    else:
        return jsonify({'message': 'Commande non trouvée'}), 404

# Ajoutez des routes pour la création, la mise à jour et la suppression des commandes

# Routes pour les marques

@app.route('/marques', methods=['GET'])
def get_marques():
    session = Session()
    marques = session.query(Marque).all()
    session.close()
    return jsonify([marque.serialize() for marque in marques])

@app.route('/marques/<int:marque_id>', methods=['GET'])
def get_marque(marque_id):
    session = Session()
    marque = session.query(Marque).get(marque_id)
    session.close()
    if marque:
        return jsonify(marque.serialize()), 200
    else:
        return jsonify({'message': 'Marque non trouvée'}), 404

# Ajoutez des routes pour la création, la mise à jour et la suppression des marques
# Point d'entrée de l'application Flask
if __name__ == '__main__':
    print("L'application Flask démarre...")
    app.run(debug=True)


    ##

    # routes.py

from flask import jsonify, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from sqlalchemy.orm import sessionmaker
from app import app
from models import Utilisateur  # Importez vos modèles de données SQLAlchemy
from database import Session

# Routes pour l'authentification

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    session = Session()
    utilisateur = session.query(Utilisateur).filter_by(email=email).first()
    session.close()
    
    if utilisateur and utilisateur.check_password(password):
        login_user(utilisateur)  # Authentifiez l'utilisateur
        return jsonify({'message': 'Connecté avec succès'}), 200
    else:
        return jsonify({'message': 'Échec de l\'authentification'}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()  # Déconnectez l'utilisateur
    return jsonify({'message': 'Déconnexion réussie'}), 200

# Routes nécessitant une authentification

@app.route('/profil')
@login_required
def profile():
    utilisateur = current_user  # Utilisez l'objet utilisateur actuellement connecté
    return jsonify(utilisateur.serialize()), 200

# Ajoutez d'autres routes nécessitant une authentification
