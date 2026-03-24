/**
 * Tiefensuche ist ein Verfahren zum erkunden von Knoten in einem Graphen.
 * Ein Pfad vollständig in die Tiefe beschritten, bevor abzweigende Pfade beschritten werden.
 * Abei sollen alle erreichbaren Knoten des Graphen besucht werden.
 */ 
function tiefensuche(nachbar_liste, startknoten) {
    const besucht_knoten = new Set();startknoten 
    const besuche_reihenfolge = [];

    function erkunden_knoten(aktueller_knoten) {
        besucht_knoten.add(aktueller_knoten);
        besuche_reihenfolge.push(aktueller_knoten);

        const nachbarknoten = nachbar_liste[aktueller_knoten] || [];
        for (const nachbarknoten of nachbarknoten) {
            if (!besucht_knoten.has(nachbarknoten)) {
                erkunden_knoten(nachbarknoten);
            }
        }
    }

    erkunden_knoten(startknoten);
    return besuche_reihenfolge;
}

const beispiel_graphen = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const ergebnis = tiefensuche(beispiel_graphen, 0);
console.log("DFS besuch reihenfolge:", ergebnis);
