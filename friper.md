# Schéma de la Base de Données de Friper

## Tables Principales

### utilisateurs
- **id**: INT (Clé primaire)
- nom: VARCHAR(100)
- email: VARCHAR(100)
- mot_de_passe: VARCHAR(100)

### produits
- **id**: INT (Clé primaire)
- nom: VARCHAR(100)
- description: TEXT
- prix: NUMERIC(10, 2)
- categorie_id: INT (Clé étrangère référençant la table categories_articles)

### commandes
- **id**: INT (Clé primaire)
- utilisateur_id: INT (Clé étrangère référençant la table utilisateurs)
- date_commande: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

### commande_produit
- commande_id: INT (Clé étrangère référençant la table commandes)
- produit_id: INT (Clé étrangère référençant la table produits)
- quantite: INT
- prix_unitaire: NUMERIC(10, 2)

## Tables Supplémentaires

### categories_articles
- **id**: INT (Clé primaire)
- nom: VARCHAR(100)

### publications_clients
- **id**: INT (Clé primaire)
- utilisateur_id: INT (Clé étrangère référençant la table utilisateurs)
- contenu: TEXT
- date_publication: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

### commentaires
- **id**: INT (Clé primaire)
- utilisateur_id: INT (Clé étrangère référençant la table utilisateurs)
- produit_id: INT (Clé étrangère référençant la table produits)
- commentaire: TEXT
- date_commentaire: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

### evaluations
- **id**: INT (Clé primaire)
- utilisateur_id: INT (Clé étrangère référençant la table utilisateurs)
- produit_id: INT (Clé étrangère référençant la table produits)
- evaluation: INT CHECK (evaluation >= 1 AND evaluation <= 5)
- date_evaluation: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

### promotions
- **id**: INT (Clé primaire)
- nom: VARCHAR(100)
- description: TEXT
- date_debut: DATE
- date_fin: DATE
- pourcentage_reduction: NUMERIC(5, 2)

## Tables de la base de données

### Table panier

La table `panier` stocke les articles ajoutés au panier par les utilisateurs.

| Champ        | Type          | Description                              |
|--------------|---------------|------------------------------------------|
| id           | SERIAL        | Identifiant unique de l'article dans le panier |
| utilisateur_id | INT           | ID de l'utilisateur qui a ajouté l'article |
| produit_id   | INT           | ID du produit ajouté au panier           |
| quantite     | INT           | Quantité de l'article ajoutée au panier  |
| date_ajout   | TIMESTAMP     | Date et heure d'ajout de l'article au panier |
| FOREIGN KEY (utilisateur_id) | INT | Clé étrangère faisant référence à la table utilisateurs |
| FOREIGN KEY (produit_id)      | INT | Clé étrangère faisant référence à la table produits |

### Table favoris

La table `favoris` stocke les articles ajoutés aux favoris par les utilisateurs.

| Champ        | Type          | Description                              |
|--------------|---------------|------------------------------------------|
| id           | SERIAL        | Identifiant unique de l'article favori  |
| utilisateur_id | INT           | ID de l'utilisateur qui a ajouté l'article aux favoris |
| produit_id   | INT           | ID du produit ajouté aux favoris        |
| date_ajout   | TIMESTAMP     | Date et heure d'ajout de l'article aux favoris |
| FOREIGN KEY (utilisateur_id) | INT | Clé étrangère faisant référence à la table utilisateurs |
| FOREIGN KEY (produit_id)      | INT | Clé étrangère faisant référence à la table produits |

### Marques

La table `marques` stocke les marques des produits.

| Champ        | Type          | Description                              |
|--------------|---------------|------------------------------------------|
| id           | SERIAL        | Identifiant unique de la marque          |
| nom          | VARCHAR(100)  | Nom de la marque                         |

### Marques_Produits

La table `marques_produits` associe les produits à leurs marques respectives.

| Champ        | Type          | Description                              |
|--------------|---------------|------------------------------------------|
| id           | SERIAL        | Identifiant unique de la relation        |
| produit_id   | INT           | ID du produit                            |
| marque_id    | INT           | ID de la marque                          |
| FOREIGN KEY (produit_id) | INT | Clé étrangère faisant référence à la table produits |
| FOREIGN KEY (marque_id)  | INT | Clé étrangère faisant référence à la table marques   |
