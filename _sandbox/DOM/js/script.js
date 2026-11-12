// Sélection par ID
const titre = document.getElementById('titre');

// Sélection par classe (retourne une NodeList)
const paragraphes = document.querySelectorAll('.paragraphe');

// Sélection par sélecteur CSS (premier match)
const bouton = document.querySelector('.btn');

// Sélection par balise
const tousLesP = document.getElementsByTagName('p');

console.log(titre);
console.log(paragraphes.length); // 2