// confirmation.js
function showConfirmationModif() {
    if (confirm("Êtes-vous sûr de vouloir modifier ce Concert ?")) {
    } else {
        event.preventDefault();
    }
}


function showConfirmationSup() {
    if (confirm("Êtes-vous sûr de vouloir Supprimer ce Concert ?")) {
    } else {
        event.preventDefault();
    }
}

function showConfirmationEnregistrer() {
    if (confirm("Êtes-vous sûr de vouloir Enregistrer ces modifications ?")) {
    } else {
        window.history.back();  // Revenir à la page précédente 
    }   
}