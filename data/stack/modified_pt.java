class Pilha {
    private int[] arrayDeElementos;
    private int topo;
    private int capacidadeDePilha;

    /** Inicializa uma pilha com a capacidade especificada. */
    public Pilha(int capacidadeDePilha) {
        this.capacidadeDePilha = capacidadeDePilha;
        this.arrayDeElementos = new int[capacidadeDePilha];
        this.topo = -1;
    }

    /** Retorna verdadeiro se a Pilha não tiver elementos. */
    public boolean estaVazia() {
        return topo == -1;
    }

    /** Retorna verdadeiro se a Pilha atingiu sua capacidade máxima. */
    public boolean estaCheia() {
        return topo == capacidadeDePilha - 1;
    }

    /** Adiciona um novo elemento acima da pilha. */
    public void empilhar(int novoElemento) {
        if (estaCheia()) {
            System.out.println("Estouro de pilha: Não é possível empilhar " + novoElemento);
            return;
        }
        arrayDeElementos[++topo] = novoElemento;
    }

    /** Remove e retorna o elemento superior da pilha. */
    public int desempilhar() {
        if (estaVazia()) {
            System.out.println("Subfluxo de pilha: A pilha está vazia");
            return -1;
        }
        return arrayDeElementos[topo--];
    }

    /** Retorna o elemento superior sem removê-lo. */
    public int topo() {
        if (estaVazia()) {
            System.out.println("A pilha está vazia");
            return -1;
        }
        return arrayDeElementos[topo];
    }

    public static void main(String[] args) {
        Pilha numberPilha = new Pilha(5);
        numberPilha.empilhar(10);
        numberPilha.empilhar(20);
        numberPilha.empilhar(30);
        System.out.println("Elemento superior: " + numberPilha.topo());
        System.out.println("Desempilhado: " + numberPilha.desempilhar());
        System.out.println("Desempilhado: " + numberPilha.desempilhar());
        System.out.println("está vazia: " + numberPilha.estaVazia());
    }
}
