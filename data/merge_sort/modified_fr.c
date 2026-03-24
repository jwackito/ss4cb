#include <stdio.h>
#include <stdlib.h>

void fusionner_moities(int tableau_de_nombres[], int index_gauche, int index_milieu, int index_droit)
{
    int taille_gauche = index_milieu - index_gauche + 1;
    int taille_droite = index_droit - index_milieu;
    int position_gauche, position_droite, position_fusionnee;

    int *gauche_temporaire = (int *)malloc(taille_gauche * sizeof(int));
    int *droit_temporaire = (int *)malloc(taille_droite * sizeof(int));

    /* Copier les données dans des tableaux temporaires */
    for (position_gauche = 0; position_gauche < taille_gauche; position_gauche++)
        gauche_temporaire[position_gauche] = tableau_de_nombres[index_gauche + position_gauche];
    for (position_droite = 0; position_droite < taille_droite; position_droite++)
        droit_temporaire[position_droite] = tableau_de_nombres[index_milieu + 1 + position_droite];

    position_gauche = 0;
    position_droite = 0;
    position_fusionnee = index_gauche;

    /* Fusionnez les deux moitiés pour les réunir dans le tableau d'origine. */
    while (position_gauche < taille_gauche && position_droite < taille_droite)
    {
        if (gauche_temporaire[position_gauche] <= droit_temporaire[position_droite])
        {
            tableau_de_nombres[position_fusionnee] = gauche_temporaire[position_gauche];
            position_gauche++;
        }
        else
        {
            tableau_de_nombres[position_fusionnee] = droit_temporaire[position_droite];
            position_droite++;
        }
        position_fusionnee++;
    }

    while (position_gauche < taille_gauche)
    {
        tableau_de_nombres[position_fusionnee] = gauche_temporaire[position_gauche];
        position_gauche++;
        position_fusionnee++;
    }
    while (position_droite < taille_droite)
    {
        tableau_de_nombres[position_fusionnee] = droit_temporaire[position_droite];
        position_droite++;
        position_fusionnee++;
    }

    free(gauche_temporaire);
    free(droit_temporaire);
}

void tri_fusion(int tableau_de_nombres[], int index_gauche, int index_droit)
{
    if (index_gauche < index_droit)
    {
        int index_milieu = index_gauche + (index_droit - index_gauche) / 2;
        tri_fusion(tableau_de_nombres, index_gauche, index_milieu);
        tri_fusion(tableau_de_nombres, index_milieu + 1, index_droit);
        fusionner_moities(tableau_de_nombres, index_gauche, index_milieu, index_droit);
    }
}

int main()
{
    int nombres[] = {38, 27, 43, 3, 9, 82, 10};
    int longueur_du_tableau = 7;
    int index;

    tri_fusion(nombres, 0, longueur_du_tableau - 1);

    printf("Tableau trié: ");
    for (index = 0; index < longueur_du_tableau; index++)
        printf("%d ", nombres[index]);
    printf("\n");
    return 0;
}
