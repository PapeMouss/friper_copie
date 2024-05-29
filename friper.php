<?php
session_start(); // Démarrage de la session

// Connexion à la base de données PostgreSQL
$host = "localhost"; // Adresse du serveur PostgreSQL
$port = "5432"; // Port PostgreSQL par défaut
$dbname = "friper_db"; // Nom de la base de données
$user = "moussamar"; // Nom d'utilisateur PostgreSQL
$connexion = pg_connect("host=$host port=$port dbname=$dbname user=$user");

if (!$connexion) {
    die("Erreur de connexion à la base de données PostgreSQL : " . pg_last_error());
}

//############################################################

// Fonction pour récupérer tous les produits depuis la base de données
function getProduits() {
    global $connexion;

    $query = "SELECT * FROM produits";
    $result = pg_query($connexion, $query);

    if (!$result) {
        die("Erreur lors de la récupération des produits: " . pg_last_error());
    }

    return $result;
}

//############################################################

// Fonction pour récupérer et afficher les publications dans la page de partage
function afficherPublications() {
    global $connexion;

    $query = "SELECT * FROM publications_clients ORDER BY date_publication DESC";
    $result = pg_query($connexion, $query);

    if (!$result) {
        die("Erreur lors de la récupération des publications: " . pg_last_error());
    }

    while ($row = pg_fetch_assoc($result)) {
        echo "<div class='publication'>";
        echo "<h3>{$row['titre']}</h3>";
        echo "<p>{$row['contenu']}</p>";
        echo "<p>Publié par {$row['auteur']} le {$row['date_publication']}</p>";
        echo "</div>";
    }
}

?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page d'accueil - Friper</title>
</head>
<body>
    <h1>Bienvenue sur Friper</h1>

    <!-- Affichage des produits -->
    <h2>Nos Produits</h2>
    <ul>
        <?php
        // Récupérer et afficher les produits disponibles
        $produits = getProduits();
        while ($row = pg_fetch_assoc($produits)) {
            echo "<li>{$row['nom']} - {$row['prix']}</li>";
        }
        ?>
    </ul>

    
    <!-- Gestion de l'authentification -->
    <?php
    if (isset($_SESSION['utilisateur_id'])) {
        // Si l'utilisateur est connecté, afficher un message de bienvenue et un lien de déconnexion
        echo "<p>Bienvenue, Utilisateur!</p>";
        echo "<a href='deconnexion.php'>Déconnexion</a>";
    } else {
        // Si l'utilisateur n'est pas connecté, afficher un lien de connexion et d'inscription
        echo "<a href='connexion.php'>Connexion</a>";
        echo "<a href='inscription.php'>Inscription</a>";
    }
    ?>

    <!-- Affichage des publications dans la page de partage -->
    <h2>Partage</h2>
    <div class="publications">
        <?php afficherPublications(); ?>
    </div>

    <!-- Filtre par catégorie -->
    <h2>Filtrer par catégorie</h2>
    <ul>
        <li><a href="categorie.php?cat=aventure_urbaine">Aventure Urbaine</a></li>
        <li><a href="categorie.php?cat=sportwear">Sportwear</a></li>
        <li><a href="categorie.php?cat=escapade_en_nature">Escapade en Nature</a></li>
        <li><a href="categorie.php?cat=voyage_au_soleil">Voyage au Soleil</a></li>
    </ul>
</body>
</html>
