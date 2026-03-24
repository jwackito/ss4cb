/**
 * Esegue una ricerca in profondità(DFS) su un grafo rappresentato come una lista di adiacenza.
 * Restituisce l'ordine in cui i nodi sono stati visitati a partire da radice.
 */
function ricerca_In_Profondita(lista_di_adiacenza, radice) { 
    const nodi_visitati = new Set();
    const ordine_di_visita = [];

    function esplora_nodo(nodo_attuale) {
        nodi_visitati.add(nodo_attuale);
        ordine_di_visita.push(nodo_attuale);

        const nodi_adiacenti = lista_di_adiacenza[nodo_attuale] || [];
        for (const nodo_adiacente of nodi_adiacenti) {
            if (!nodi_visitati.has(nodo_adiacente)) {
                esplora_nodo(nodo_adiacente);
            }
        }
    }

    esplora_nodo(radice);
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

const risultato = ricerca_In_Profondita(esempio_di_grafo, 0);
console.log("DFS ordine di visita:", risultato);
