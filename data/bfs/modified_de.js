/**
 * Führt eine Breitensuche auf einem Graphen durch, der als Adjazenzliste dargestellt ist.
 * Gibt die Reihenfolge zurück, in der Knoten besucht wurden, beginnend mit Startknoten.
 */
function breitensuche(adjazenz_liste, startknoten) {
    const besuchte_knoten  = new Set();
    const warteschlange = [];
    const besuchsreihenfolge = [];

    besuchte_knoten .add(startknoten);
    warteschlange.push(startknoten);

    while (warteschlange.length > 0) {
        const aktueller_knoten = warteschlange.shift();
        besuchsreihenfolge.push(aktueller_knoten);

        const nachbar_liste = adjazenz_liste[aktueller_knoten] || [];
        for (const nachbarknoten of nachbar_liste) {
            if (!besuchte_knoten .has(nachbarknoten)) {
                besuchte_knoten .add(nachbarknoten);
                warteschlange.push(nachbarknoten);
            }
        }
    }

    return besuchsreihenfolge;
}

const beispiel_graphen = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const ergebnis = breitensuche(beispiel_graphen, 0);
console.log("BFS besuch reihenfolge:", ergebnis);
