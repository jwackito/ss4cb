class Pile {
    private int[] tableauDElements;
    private int indexSuperieur;
    private int capacitePile;

    /** Initialise une pile avec la capacité donnée */
    public Pile(int capacitePile) {
        this.capacitePile = capacitePile;
        this.tableauDElements = new int[capacitePile];
        this.indexSuperieur = -1;
    }

    /** Renvoie vrai si la pile ne contient aucun élément */
    public boolean estVide() {
        return indexSuperieur == -1;
    }

    /** Renvoie vrai si la pile a atteint sa capacité maximale. */
    public boolean estPleine() {
        return indexSuperieur == capacitePile - 1;
    }

    /** Ajoute un nouvel élément au-dessus de la pile */
    public void empiler(int nouvelElement) {
        if (estPleine()) {
            System.out.println("Dépassement de pile : impossible d'empiler " + nouvelElement);
            return;
        }
        tableauDElements[++indexSuperieur] = nouvelElement;
    }

    /** Supprime et renvoie l'élément supérieur de la pile. */
    public int depiler() {
        if (estVide()) {
            System.out.println("Sous-passement de pile : la pile est vide");
            return -1;
        }
        return tableauDElements[indexSuperieur--];
    }

    /** envoie l'élément supérieur sans le supprimer. */
    public int sommet() {
        if (estVide()) {
            System.out.println("Pile est vide");
            return -1;
        }
        return tableauDElements[indexSuperieur];
    }

    public static void main(String[] args) {
        Pile nombrePile = new Pile(5);
        nombrePile.empiler(10);
        nombrePile.empiler(20);
        nombrePile.empiler(30);
        System.out.println("Élément supérieur: " + nombrePile.sommet());
        System.out.println("Dépilé: " + nombrePile.depiler());
        System.out.println("Dépilé: " + nombrePile.depiler());
        System.out.println("Est vide: " + nombrePile.estVide());
    }
}
