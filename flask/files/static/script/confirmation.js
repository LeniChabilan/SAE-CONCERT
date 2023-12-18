// confirmation.js
function showConfirmationModif() {
    if (confirm("Êtes-vous sûr de vouloir modifier ce Concert ?")) {
    } else {
        window.history.back();  // Revenir à la page précédente
    }
}


function showConfirmationSup() {
    if (confirm("Êtes-vous sûr de vouloir Supprimer ce Concert ?")) {
    } else {
        window.history.back();  // Revenir à la page précédente
    }
}

function showConfirmationEnregistrer() {
    if (confirm("Êtes-vous sûr de vouloir Enregistrer ces modifications ?")) {
    } else {
        window.history.back();  // Revenir à la page précédente 
    }   
}

function showConfirmationSupGroupe() {
    if (confirm("Êtes-vous sûr de vouloir Supprimer ce Groupe ?")) {
    } else {
        window.history.back();  // Revenir à la page précédente
    }
}