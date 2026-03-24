/**
 * Effectue une recherche en largeur sur un graphe représenté sous forme de liste d'adjacence.
 * Renvoie l'ordre de visite des nœuds à partir de sommet_depart.
 */
function algorithmeDeParcoursEnLargeur(liste_voisins, sommet_depart) {
    const sommets_visites = new Set();
    const file = [];
    const ordre_visite  = [];

    sommets_visites.add(sommet_depart);
    file.push(sommet_depart);

    while (file.length > 0) {
        const sommet_actuel = file.shift();
        ordre_visite .push(sommet_actuel);

        const voisins_sommets = liste_voisins[sommet_actuel] || [];
        for (const voisin_sommet of voisins_sommets) {
            if (!sommets_visites.has(voisin_sommet)) {
                sommets_visites.add(voisin_sommet);
                file.push(voisin_sommet);
            }
        }
    }

    return ordre_visite ;
}

const exemple_graphe = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultat = algorithmeDeParcoursEnLargeur(exemple_graphe, 0);
console.log("BFS visite ordre:", resultat);
