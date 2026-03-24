class VerketteteListe {

    private static class Listenknoten {
        int knotenWert;

        Listenknoten naechsterKnoten;

        Listenknoten(int knotenWert) {
            this.knotenWert = knotenWert;
            this.naechsterKnoten = null;
        }
    }

    private Listenknoten kopfKnoten;

    /** Fügt am Ende der Liste einen neuen Knoten mit dem Wert ein. */
    public void amEndeEinfuegen(int neuerWert) {
        Listenknoten neuerKnoten = new Listenknoten(neuerWert);
        if (kopfKnoten == null) {
            kopfKnoten = neuerKnoten;
            return;
        }
        Listenknoten aktuellerKnoten = kopfKnoten;
        while (aktuellerKnoten.naechsterKnoten != null) {
            aktuellerKnoten = aktuellerKnoten.naechsterKnoten;
        }
        aktuellerKnoten.naechsterKnoten = neuerKnoten;
    }

    /** Löscht den ersten gefundenen Knoten mit dem angegebenen Zielwert. */
    public void loeschenNachWert(int zielWert) {
        if (kopfKnoten == null)
            return;
        if (kopfKnoten.knotenWert == zielWert) {
            kopfKnoten = kopfKnoten.naechsterKnoten;
            return;
        }
        Listenknoten aktuellerKnoten = kopfKnoten;
        while (aktuellerKnoten.naechsterKnoten != null) {
            if (aktuellerKnoten.naechsterKnoten.knotenWert == zielWert) {
                aktuellerKnoten.naechsterKnoten = aktuellerKnoten.naechsterKnoten.naechsterKnoten;
                return;
            }
            aktuellerKnoten = aktuellerKnoten.naechsterKnoten;
        }
    }

    /** Gibt alle Knotenwerte von Kopf bis Ende aus */
    public void listeDrucken() {
        Listenknoten aktuellerKnoten = kopfKnoten;
        while (aktuellerKnoten != null) {
            System.out.print(aktuellerKnoten.knotenWert + " -> ");
            aktuellerKnoten = aktuellerKnoten.naechsterKnoten;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        VerketteteListe nummernListe = new VerketteteListe();
        nummernListe.amEndeEinfuegen(10);
        nummernListe.amEndeEinfuegen(20);
        nummernListe.amEndeEinfuegen(30);
        nummernListe.amEndeEinfuegen(40);
        System.out.print("liste: ");
        nummernListe.listeDrucken();
        nummernListe.loeschenNachWert(20);
        System.out.print("Nach dem Löschen von 20: ");
        nummernListe.listeDrucken();
    }
}
