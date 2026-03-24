#include <stdio.h>

void tri_a_bulles(int tableau_nombres[], int tableau_length)
{
    /* trier tableau_nombres en ordre croissant à l'aide de bubble trier */
    int passage_exterieur;
    int passage_interieur;
    int valeur_temporaire;
    int echange;

    for (passage_exterieur = 0; passage_exterieur < tableau_length - 1; passage_exterieur++)
    {
        echange = 0;
        for (passage_interieur = 0; passage_interieur < tableau_length - passage_exterieur - 1; passage_interieur++)
        {
            if (tableau_nombres[passage_interieur] > tableau_nombres[passage_interieur + 1])
            {
                /* permuter les éléments adjacents */
                valeur_temporaire = tableau_nombres[passage_interieur];
                tableau_nombres[passage_interieur] = tableau_nombres[passage_interieur + 1];
                tableau_nombres[passage_interieur + 1] = valeur_temporaire;
                echange = 1;
            }
        }
        /* Si aucun échange n'a eu lieu lors de cette passe, le tableau est déjà trié. */
        if (echange == 0)
            break;
    }
}

int main()
{
    int nombres[] = {64, 34, 25, 12, 22, 11, 90};
    int tableau_length = 7;
    int indice;

    tri_a_bulles(nombres, tableau_length);

    printf("trie tableau: ");
    for (indice = 0; indice < tableau_length; indice++)
    {
        printf("%d ", nombres[indice]);
    }
    printf("\n");
    return 0;
}
