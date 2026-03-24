/**
 * Realiza una Busqueda En Profundidad(DFS) en un grafo representado como una lista de adyacencia.
 * Retorna el orden en el cual los nodos fueron visitados empezando por el nodo_inicio.
 */
function BusquedaEnProfundidad(listado_de_adyacencia, nodo_inicio) {
    const nodos_visitados = new Set();
    const orden_de_visita = [];

    function explorar_nodo(nodo_actual) {
        nodos_visitados.add(nodo_actual);
        orden_de_visita.push(nodo_actual);

        const nodos_vecinos = listado_de_adyacencia[nodo_actual] || [];
        for (const nodo_vecino of nodos_vecinos) {
            if (!nodos_visitados.has(nodo_vecino)) {
                explorar_nodo(nodo_vecino);
            }
        }
    }

    explorar_nodo(nodo_inicio);
    return orden_de_visita;
}

const grafo_ejemplo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultado = BusquedaEnProfundidad(grafo_ejemplo, 0);
console.log("Orden de visita de DFS:", resultado);
