/**
 * Esegue una ricerca in ampiezza su un grafo rappresentato come una lista di adiacenza.
 * Restituisce l'ordine in cui i nodi sono stati visitati a partire dalla nodo_partenza.
 */
function ricerca_in_ampiezza(lista_di_adiacenza, nodo_partenza ) { 
    const nodi_visitati = new Set();
    const coda = [];
    const ordine_di_visita = [];

    nodi_visitati.add(nodo_partenza );
    coda.push(nodo_partenza );

    while (coda.length > 0) {
        const nodo_attuale = coda.shift();
        ordine_di_visita.push(nodo_attuale);

        const nodi_adiacenti = lista_di_adiacenza[nodo_attuale] || [];
        for (const nodo_adiacente of nodi_adiacenti) {
            if (!nodi_visitati.has(nodo_adiacente)) {
                nodi_visitati.add(nodo_adiacente);
                coda.push(nodo_adiacente);
            }
        }
    }

    return ordine_di_visita;
}

const esempio_di_grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const risultato = ricerca_in_ampiezza(esempio_di_grafo, 0);
console.log("BFS visita ordinata:", risultato);
