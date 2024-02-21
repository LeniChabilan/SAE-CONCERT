

function validateForm() {
    var dateDNInput = document.forms["myForm"]["dateDN"].value;
    var numSecInput = document.forms["myForm"]["numSec"].value;
    var numCNIInput = document.forms["myForm"]["numCNI"].value;
    var dateDelivre = document.forms["myForm"]["dateDelivrance"].value;
    var dateExpire = document.forms["myForm"]["dateExpiration"].value;

    console.log(dateDelivre);
    var selectedDate = new Date(dateDNInput);
    
    var dateDelivre = new Date(dateDelivre);
    var dateExpire = new Date(dateExpire);
    var currentDate = new Date();
  
    if (selectedDate > currentDate) {
      alert("La date de naissance doit être antérieure à la date actuelle.");
      return false;
    }
  
    if (numSecInput.length !=15 || numCNIInput.length != 15) {
      alert("Les numéros de sécurité sociale et CNI doivent avoir une longueur egale à 15.");
      return false;
    }

    if (dateDelivre > dateExpire) {
      alert("La date de délivrance de la CNI doit être antérieure à la date d'expiration.");
      return false;
    }

    if(dateDelivre > currentDate){
      alert("La date de délivrance de la CNI doit être antérieure à la date actuelle.");
      return false;
    }

    if(dateExpire < currentDate){
      alert("La carte n'est plus valide.");
      return false;
    }

    var dateDelivrePlus10Ans = new Date(dateDelivre);
    dateDelivrePlus10Ans.setFullYear(dateDelivrePlus10Ans.getFullYear() + 10);

    if(dateExpire.getTime() < dateDelivrePlus10Ans.getTime()){
        alert("La date d'expiration de la CNI doit être exactement 10 ans après la date de délivrance.");
        return false;
    }

  
    return true;
}

