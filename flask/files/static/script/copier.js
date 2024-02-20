function copierTexteDansPressePapiers() {
    var texte= document.getElementsByClassName("idConcert")[0].value;
    var texteACopier = "127.0.0.1:5000/accueil_artiste.html/"+texte;
    var texteTemporaire = document.createElement("textarea");
    texteTemporaire.value = texteACopier;
    document.body.appendChild(texteTemporaire);
    texteTemporaire.select();
    document.execCommand("copy");
    document.body.removeChild(texteTemporaire);
  
    var bouton = document.getElementById("boutonCopier");
    bouton.innerHTML = "Lien copié !";

    setTimeout(function () {
    bouton.innerHTML = "Copier le lien du formulaire";
  }, 500);
}
  