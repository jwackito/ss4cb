class Pila {
    private int[] elementiArray;
    private int indiceSuperiore;
    private int pilaCapacita;

    /** Inizializza una la pila con la capacità specificata */
    public Pila(int pilaCapacita) {
        this.pilaCapacita = pilaCapacita;
        this.elementiArray = new int[pilaCapacita];
        this.indiceSuperiore = -1;
    }

    /** Restituisce true se la pila non ha elementi */
    public boolean eVuoto() {
        return indiceSuperiore == -1;
    }

    /** Restituisce true se la pila ha raggiunto la sua capacità */
    public boolean ePieno() {
        return indiceSuperiore == pilaCapacita - 1;
    }

    /** Aggiunge un nuovo elemento sopra il pila */
    public void Inserire(int nuovoElemento) {
        if (ePieno()) {
            System.out.println("Pila piena: impossibile inserire " + nuovoElemento);
            return;
        }
        elementiArray[++indiceSuperiore] = nuovoElemento;
    }

    /** Rimuove e restituisce l'elemento superiore del pila */
    public int Estrarre() {
        if (eVuoto()) {
            System.out.println("Pila vuota: Pila è vuota");
            return -1;
        }
        return elementiArray[indiceSuperiore--];
    }

    /** Restituisce l'elemento superiore senza rimuoverlo */
    public int visualizza() {
        if (eVuoto()) {
            System.out.println("Pila è vuota");
            return -1;
        }
        return elementiArray[indiceSuperiore];
    }

    public static void main(String[] args) {
        Pila numeroPila = new Pila(5);
        numeroPila.Inserire(10);
        numeroPila.Inserire(20);
        numeroPila.Inserire(30);
        System.out.println("Elemento superiore: " + numeroPila.visualizza());
        System.out.println("Estratto: " + numeroPila.Estrarre());
        System.out.println("Estratto: " + numeroPila.Estrarre());
        System.out.println("È vuota: " + numeroPila.eVuoto());
    }
}
