fetch('/api/utilisateurs')
  .then(response => {
    if (!response.ok) {
      throw new Error('Erreur lors de la récupération des données');
    }
    return response.json();
  })
  .then(data => {
    // Traitez les données récupérées
    console.log(data);
  })
  .catch(error => {
    // Gérez les erreurs
    console.error('Erreur :', error);
  });