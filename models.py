# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'

    id = Column(Integer, primary_key=True)
    nom = Column(String)
    email = Column(String)
    mot_de_passe = Column(String)

    commandes = relationship("Commande", back_populates="utilisateur")
    favoris = relationship("Favori", back_populates="utilisateur")


     def check_password(self, mot_de_passe):
        return self.mot_de_passe == mot_de_passe

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

# Définissez les autres classes de modèle de données de la même manière

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