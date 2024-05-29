from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Définir le modèle d'utilisateur si vous l'avez
from models import User  # Assurez-vous d'avoir défini le modèle d'utilisateur dans un fichier models.py

db_username = 'moussamar'
db_host = 'localhost'
db_name = 'friper_db'

# Créez l'URL de connexion à la base de données
db_url = f'postgresql://{db_username}@{db_host}/{db_name}'

# Créez le moteur SQLAlchemy
engine = create_engine(db_url)

# Créez une classe de session pour interagir avec la base de données
Session = sessionmaker(bind=engine)

# Créez une instance de session
session = Session()

# Requêtes test
# Exemple de requête SQL
result = session.execute('SELECT * FROM utilisateurs')
print("Résultat de la requête SELECT * FROM utilisateurs :")
for row in result:
    print(row)

# Exemple de création d'une nouvelle entrée dans la table "utilisateurs"
new_user = User(name='John', email='john@example.com')  # Assurez-vous que la classe User est définie correctement
session.add(new_user)
session.commit()
print("Nouvel utilisateur ajouté avec succès.")

# Fermez la session lorsque vous avez terminé
session.close()


from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Créez une instance de declarative_base()
Base = declarative_base()

# Définissez les modèles de données pour chaque table

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)

    commandes = relationship("Commande", back_populates="utilisateur")
    favoris = relationship("Favori", back_populates="utilisateur")

class ArticleCategorie(Base):
    __tablename__ = 'article_categorie'

    id = Column(Integer, primary_key=True)
    nom = Column(String)

    articles = relationship("CategorieArticle", back_populates="categorie")

class CategorieArticle(Base):
    __tablename__ = 'categories_articles'

    id = Column(Integer, primary_key=True)
    categorie_id = Column(Integer, ForeignKey('article_categorie.id'))
    article_id = Column(Integer, ForeignKey('produits.id'))

    categorie = relationship("ArticleCategorie", back_populates="articles")
    article = relationship("Produit", back_populates="categories")

class Produit(Base):
    __tablename__ = 'produits'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    description = Column(String)
    prix = Column(Float)
    marque_id = Column(Integer, ForeignKey('marques.id'))

    marque = relationship("Marque", back_populates="produits")
    categories = relationship("CategorieArticle", back_populates="article")
    evaluations = relationship("Evaluation", back_populates="produit")
    commandes = relationship("CommandeProduit", back_populates="produit")

class Marque(Base):
    __tablename__ = 'marques'

    id = Column(Integer, primary_key=True)
    nom = Column(String)

    produits = relationship("Produit", back_populates="marque")

class Commande(Base):
    __tablename__ = 'commandes'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    date_commande = Column(DateTime)
    total = Column(Float)
    statut = Column(String)

    utilisateur = relationship("Utilisateur", back_populates="commandes")
    produits = relationship("CommandeProduit", back_populates="commande")

class CommandeProduit(Base):
    __tablename__ = 'commande_produit'

    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey('commandes.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    quantite = Column(Integer)
    prix_unitaire = Column(Float)

    commande = relationship("Commande", back_populates="produits")
    produit = relationship("Produit", back_populates="commandes")

class Favori(Base):
    __tablename__ = 'favoris'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))

    utilisateur = relationship("Utilisateur", back_populates="favoris")
    produit = relationship("Produit", back_populates="favoris")

class Evaluation(Base):
    __tablename__ = 'evaluations'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    note = Column(Integer)
    commentaire = Column(String)

    utilisateur = relationship("Utilisateur", back_populates="evaluations")
    produit = relationship("Produit", back_populates="evaluations")

class Commentaire(Base):
    __tablename__ = 'commentaires'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    texte = Column(String)
    date_creation = Column(DateTime)
    est_visible = Column(Boolean)

    utilisateur = relationship("Utilisateur", back_populates="commentaires")
    produit = relationship("Produit", back_populates="commentaires")

class Promotion(Base):
    __tablename__ = 'promotions'

    id = Column(Integer, primary_key=True)
    produit_id = Column(Integer, ForeignKey('produits.id'))
    pourcentage_reduction = Column(Float)
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)

    produit = relationship("Produit", back_populates="promotions")

class Panier(Base):
    __tablename__ = 'panier'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    produit_id = Column(Integer, ForeignKey('produits.id'))
    quantite = Column(Integer)

    utilisateur = relationship("Utilisateur", back_populates="panier")
    produit = relationship("Produit", back_populates="panier")

class PublicationClient(Base):
    __tablename__ = 'publications_clients'

    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey('utilisateurs.id'))
    texte = Column(String)
    date_creation = Column(DateTime)

    utilisateur = relationship("Utilisateur", back_populates="publications_clients")


###############################
#implémentation fonctionnallittés bbackend avec flask

from flask import Flask

if __name__ == '__main__':
    print("L'application démarre...")
    app.run(debug=True)


from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Utilisateur, Produit, Commande, Marque  # Importez les modèles que vous avez définis

print("L'application Flask démarre...")


# Créez une instance de l'application Flask
app = Flask(__name__)

# Configurez la connexion à la base de données PostgreSQL
db_username = 'moussamar'
db_host = 'localhost'
db_name = 'friper_db'
db_url = f'postgresql://{db_username}@{db_host}/{db_name}'

# Créez le moteur SQLAlchemy
engine = create_engine(db_url)

# Créez une classe de session pour interagir avec la base de données
Session = sessionmaker(bind=engine)

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

@app.route('/utilisateurs', methods=['POST'])
def create_utilisateur():
    data = request.json
    nouvel_utilisateur = Utilisateur(nom=data['nom'], email=data['email'])
    session = Session()
    session.add(nouvel_utilisateur)
    session.commit()
    session.close()
    return jsonify(nouvel_utilisateur.serialize()), 201

####
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