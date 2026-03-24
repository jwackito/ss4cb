class ListeChainee {

    private static class Maillon {
        int donnee;
        Maillon noeudSuivant;

        Maillon(int donnee) {
            this.donnee = donnee;
            this.noeudSuivant = null;
        }
    }

    private Maillon noeudTete;

    /** Insère un nouveau noeud avec une valeur à la fin de la liste */
    public void insererALaFin(int nouvelleValeur) {
        Maillon nouveauNoeud = new Maillon(nouvelleValeur);
        if (noeudTete == null) {
            noeudTete = nouveauNoeud;
            return;
        }
        Maillon noeudActuel = noeudTete;
        while (noeudActuel.noeudSuivant != null) {
            noeudActuel = noeudActuel.noeudSuivant;
        }
        noeudActuel.noeudSuivant = nouveauNoeud;
    }

    /** Supprime le premier noeud trouvé avec la valeur cible donnée. */
    public void supprimerParValeur(int valeurCible) {
        if (noeudTete == null)
            return;
        if (noeudTete.donnee == valeurCible) {
            noeudTete = noeudTete.noeudSuivant;
            return;
        }
        Maillon noeudActuel = noeudTete;
        while (noeudActuel.noeudSuivant != null) {
            if (noeudActuel.noeudSuivant.donnee == valeurCible) {
                noeudActuel.noeudSuivant = noeudActuel.noeudSuivant.noeudSuivant;
                return;
            }
            noeudActuel = noeudActuel.noeudSuivant;
        }
    }

    /** Affiche toutes les valeurs des noeuds de la tête à la queue */
    public void imprimerListe() {
        Maillon noeudActuel = noeudTete;
        while (noeudActuel != null) {
            System.out.print(noeudActuel.donnee + " -> ");
            noeudActuel = noeudActuel.noeudSuivant;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        ListeChainee listeDeNombres = new ListeChainee();
        listeDeNombres.insererALaFin(10);
        listeDeNombres.insererALaFin(20);
        listeDeNombres.insererALaFin(30);
        listeDeNombres.insererALaFin(40);
        System.out.print("Liste: ");
        listeDeNombres.imprimerListe();
        listeDeNombres.supprimerParValeur(20);
        System.out.print("Après avoir supprimé 20: ");
        listeDeNombres.imprimerListe();
    }
}
