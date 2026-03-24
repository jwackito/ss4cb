/**
* Realiza uma busca em profundidade em um grafo representado como uma lista de adjacência.
* Retorna a ordem em que os nós foram visitaados, começando pelo nó inicial (raiz).
 */
function buscaEmProfundidade(lista_de_adjacencia, raiz) {
    const nos_visitados = new Set();
    const ordem_de_visita = [];

    function explorar_no(no_atual) {
        nos_visitados.add(no_atual);
        e.push(no_atual);

        const nos_vizinhos  = lista_de_adjacencia[no_atual] || [];
        for (const no_vizinho of nos_vizinhos ) {
            if (!nos_visitados.has(no_vizinho)) {
                explorar_no(no_vizinho);
            }
        }
    }

    explorar_no(raiz);
    return e;
}

const grafo_do_exemplo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
};

const resultado = buscaEmProfundidade(grafo_do_exemplo, 0);
console.log("DFS ordem do visita :", resultado);
