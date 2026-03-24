class ListaEncadeada {

    private static class NoDaLista {
        int valorDoNo;

        NoDaLista proximoNo;

        NoDaLista(int valorDoNo) {
            this.valorDoNo = valorDoNo;
            this.proximoNo = null;
        }
    }

    private NoDaLista noCabeca;

    /** Insere um novo nó com valor no final da lista. */
    public void inserirNoFim(int novoValor) {
        NoDaLista novoNo = new NoDaLista(novoValor);
        if (noCabeca == null) {
            noCabeca = novoNo;
            return;
        }
        NoDaLista noAtual = noCabeca;
        while (noAtual.proximoNo != null) {
            noAtual = noAtual.proximoNo;
        }
        noAtual.proximoNo = novoNo;
    }

    /** Exclui o primeiro nó encontrado com o valor alvo fornecido. */
    public void excluirPorValor(int valorAlvo) {
        if (noCabeca == null)
            return;
        if (noCabeca.valorDoNo == valorAlvo) {
            noCabeca = noCabeca.proximoNo;
            return;
        }
        NoDaLista noAtual = noCabeca;
        while (noAtual.proximoNo != null) {
            if (noAtual.proximoNo.valorDoNo == valorAlvo) {
                noAtual.proximoNo = noAtual.proximoNo.proximoNo;
                return;
            }
            noAtual = noAtual.proximoNo;
        }
    }

    /** Imprime todos os valores dos nós, da cabeca à cauda. */
    public void imprimirLista() {
        NoDaLista noAtual = noCabeca;
        while (noAtual != null) {
            System.out.print(noAtual.valorDoNo + " -> ");
            noAtual = noAtual.proximoNo;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListaEncadeada listaDeNumeros = new ListaEncadeada();
        listaDeNumeros.inserirNoFim(10);
        listaDeNumeros.inserirNoFim(20);
        listaDeNumeros.inserirNoFim(30);
        listaDeNumeros.inserirNoFim(40);
        System.out.print("List: ");
        listaDeNumeros.imprimirLista();
        listaDeNumeros.excluirPorValor(20);
        System.out.print("After deleting 20: ");
        listaDeNumeros.imprimirLista();
    }
}
