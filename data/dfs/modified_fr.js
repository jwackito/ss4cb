/**
 * Effectue un parcours_en_profondeur(DFS) sur un graphe représenté comme une liste de voisins. 
 * Renvoie l'ordre dans lequel les sommets ont été visités début de sommet_depart.
 */
function parcours_en_profondeur(liste_voisins, sommet_depart) {
    const deja_visite_sommets = new Set();
    const ordre_visite = [];

    function explorer_sommet(actuel_sommet) {
        deja_visite_sommets.add(actuel_sommet);
        ordre_visite.push(actuel_sommet);

        const voisins_sommets = liste_voisins[actuel_sommet] || [];
        for (const voisin_sommet of voisins_sommets) {
            if (!deja_visite_sommets.has(voisin_sommet)) {
                explorer_sommet(voisin_sommet);
            }
        }
    }

    explorer_sommet(sommet_depart);
    return ordre_visite;
}

const exemple_graphe = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultat = parcours_en_profondeur(exemple_graphe, 0);
console.log("DFS visite ordre:", resultat);
