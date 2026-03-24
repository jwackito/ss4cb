#include <stdio.h>

void echanger_elements(int *premier_element, int *deuxieme_element)
{
    int valeur_temporaire = *premier_element;
    *premier_element = *deuxieme_element;
    *deuxieme_element = valeur_temporaire;
}

int tableau_partition(int tableau_de_nombres[], int indice_bas, int indice_eleve)
{
    int valeur_pivot = tableau_de_nombres[indice_eleve];
    int indice_element_plus_petit = indice_bas - 1;
    int indice_actuel;

    for (indice_actuel = indice_bas; indice_actuel < indice_eleve; indice_actuel++)
    {
        if (tableau_de_nombres[indice_actuel] <= valeur_pivot)
        {
            indice_element_plus_petit++;
            echanger_elements(&tableau_de_nombres[indice_element_plus_petit], &tableau_de_nombres[indice_actuel]);
        }
    }
    echanger_elements(&tableau_de_nombres[indice_element_plus_petit + 1], &tableau_de_nombres[indice_eleve]);
    return indice_element_plus_petit + 1;
}

void tri_rapide(int tableau_de_nombres[], int indice_bas, int indice_eleve)
{
    if (indice_bas < indice_eleve)
    {
        int pivot_indice = tableau_partition(tableau_de_nombres, indice_bas, indice_eleve);
        tri_rapide(tableau_de_nombres, indice_bas, pivot_indice - 1);
        tri_rapide(tableau_de_nombres, pivot_indice + 1, indice_eleve);
    }
}

int main()
{
    int nombres[] = {10, 7, 8, 9, 1, 5};
    int longueur_du_tableau = 6;
    int indice;

    tri_rapide(nombres, 0, longueur_du_tableau - 1);

    printf("Tableau trié: ");
    for (indice = 0; indice < longueur_du_tableau; indice++)
        printf("%d ", nombres[indice]);
    printf("\n");
    return 0;
}
