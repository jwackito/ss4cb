/**
 * Executa uma busca em largura (BFS) em um grafo representado como uma lista de adjacência.
 * Retorna a ordem em que os nós foram visitados, começando pela no_inicial.
 */
function buscaEmLargura(lista_de_adjacencia, no_inicial) {
    const nos_visitados = new Set();
    const fila = [];
    const ordem_de_visita = [];

    nos_visitados.add(no_inicial);
    fila.push(no_inicial);

    while (fila.length > 0) {
        const no_atual = fila.shift();
        ordem_de_visita.push(no_atual);

        const nos_vizinhos = lista_de_adjacencia[no_atual] || [];
        for (const no_vizinho of nos_vizinhos) {
            if (!nos_visitados.has(no_vizinho)) {
                nos_visitados.add(no_vizinho);
                fila.push(no_vizinho );
            }
        }
    }

    return ordem_de_visita;
}

const grafo_do_exemplo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultado = buscaEmLargura(grafo_do_exemplo, 0);
console.log("BFS ordem de visita:", resultado );
