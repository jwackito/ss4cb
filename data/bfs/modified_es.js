/**
 * Realiza Búsqueda en Anchura en un grafo representado como una lista de adyacencia.
 * Retorna el orden en el cual los nodos fueron visitados empezando por nodo_inicial
 */
function busquedaEnAnchura(lista_adyacentes, nodo_inicial) {
    const nodos_visitados = new Set();
    const cola = [];
    const orden_de_visitas = [];

    nodos_visitados.add(nodo_inicial);
    cola.push(nodo_inicial);

    while (cola.length > 0) {
        const nodo_actual = cola.shift();
        orden_de_visitas.push(nodo_actual);

        const nodos_vecinos = lista_adyacentes[nodo_actual] || [];
        for (const nodo_vecino of nodos_vecinos) {
            if (!nodos_visitados.has(nodo_vecino)) {
                nodos_visitados.add(nodo_vecino);
                cola.push(nodo_vecino);
            }
        }
    }

    return orden_de_visitas;
}

const grafo_de_ejemplo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultado = busquedaEnAnchura(grafo_de_ejemplo, 0);
console.log("BFS orden de visitas:", resultado);
