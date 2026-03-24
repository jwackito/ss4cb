class Stapel {
    private int[] elementenArray;
    private int obersterIndex;
    private int stapelKapazitaet;

    /** Initializes a Stapel with the given capacity */
    public Stapel(int stapelKapazitaet) {
        this.stapelKapazitaet = stapelKapazitaet;
        this.elementenArray = new int[stapelKapazitaet];
        this.obersterIndex = -1;
    }

    /** Gibt true zurück, wenn der Stapel keine Elemente enthält. */
    public boolean istLeer() {
        return obersterIndex == -1;
    }

    /** Gibt true zurück, wenn der Stapel seine Kapazität erreicht hat. */
    public boolean istVoll() {
        return obersterIndex == stapelKapazitaet - 1;
    }

    /** Fügt dem stapel ein neues Element hinzu. */
    public void hinzufuegen(int neuesElement) {
        if (istVoll()) {
            System.out.println("Stapelüberlauf: Kann nicht hinzugefügt werden" + neuesElement);
            return;
        }
        elementenArray[++obersterIndex] = neuesElement;
    }

    /** Entfernt und gibt das oberste Element des Stapels zurück. */
    public int entfernen() {
        if (istLeer()) {
            System.out.println("Stapel-Unterlauf: Stapel ist leer");
            return -1;
        }
        return elementenArray[obersterIndex--];
    }

    /** Gibt das oberste Element zurück, ohne es zu entfernen. */
    public int oberstesElement() {
        if (istLeer()) {
            System.out.println("Stapel ist leer");
            return -1;
        }
        return elementenArray[obersterIndex];
    }

    public static void main(String[] args) {
        Stapel nummerStapel = new Stapel(5);
        nummerStapel.hinzufuegen(10);
        nummerStapel.hinzufuegen(20);
        nummerStapel.hinzufuegen(30);
        System.out.println("Oberes Element: " + nummerStapel.oberstesElement());
        System.out.println("Entnommen: " + nummerStapel.entfernen());
        System.out.println("Entnommen: " + nummerStapel.entfernen());
        System.out.println("Ist leer: " + nummerStapel.istLeer());
    }
}
