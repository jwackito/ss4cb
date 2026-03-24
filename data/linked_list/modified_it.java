class ListaConcatenata {

    private static class NodoLista {
        int valoreNodo;
        NodoLista nodoSuccessivo;

        NodoLista(int valoreNodo) {
            this.valoreNodo = valoreNodo;
            this.nodoSuccessivo = null;
        }
    }

    private NodoLista nodoTesta;

    /** Inserisce un nuovo nodo con valore alla fine dell'elenco. */
    public void inserireAllaFine(int nuovoValore) {
        NodoLista nuovoNodo = new NodoLista(nuovoValore);
        if (nodoTesta == null) {
            nodoTesta = nuovoNodo;
            return;
        }
        NodoLista nodoAttuale = nodoTesta;
        while (nodoAttuale.nodoSuccessivo != null) {
            nodoAttuale = nodoAttuale.nodoSuccessivo;
        }
        nodoAttuale.nodoSuccessivo = nuovoNodo;
    }

    /** Elimina il primo nodo trovato con il valore valoreObiettivo specificato */
    public void eliminaPerValore(int valoreObiettivo) {
        if (nodoTesta == null)
            return;
        if (nodoTesta.valoreNodo == valoreObiettivo) {
            nodoTesta = nodoTesta.nodoSuccessivo;
            return;
        }
        NodoLista nodoAttuale = nodoTesta;
        while (nodoAttuale.nodoSuccessivo != null) {
            if (nodoAttuale.nodoSuccessivo.valoreNodo == valoreObiettivo) {
                nodoAttuale.nodoSuccessivo = nodoAttuale.nodoSuccessivo.nodoSuccessivo;
                return;
            }
            nodoAttuale = nodoAttuale.nodoSuccessivo;
        }
    }

    /** Stampa tutti i valori dei nodi dalla testa alla coda */
    public void stampaLista() {
        NodoLista nodoAttuale = nodoTesta;
        while (nodoAttuale != null) {
            System.out.print(nodoAttuale.valoreNodo + " -> ");
            nodoAttuale = nodoAttuale.nodoSuccessivo;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListaConcatenata listaDiNumeri = new ListaConcatenata();
        listaDiNumeri.inserireAllaFine(10);
        listaDiNumeri.inserireAllaFine(20);
        listaDiNumeri.inserireAllaFine(30);
        listaDiNumeri.inserireAllaFine(40);
        System.out.print("Lista: ");
        listaDiNumeri.stampaLista();
        listaDiNumeri.eliminaPerValore(20);
        System.out.print("Dopo aver eliminato 20: ");
        listaDiNumeri.stampaLista();
    }
}
