#include <stdio.h>
#include <stdlib.h>

void fondi_sottoarray(int vettore_di_numeri[], int indice_sinistra, int indice_mezzo, int indice_destro)
{
    int dimensione_sinistra = indice_mezzo - indice_sinistra + 1;
    int dimensione_destra = indice_destro - indice_mezzo;
    int posizione_sinistra, posizione_destra, posizione_unita;

    int *sinistra_temp = (int *)malloc(dimensione_sinistra * sizeof(int));
    int *destro_temp = (int *)malloc(dimensione_destra * sizeof(int));

    /* Copia i dati in vettore temporanei */
    for (posizione_sinistra = 0; posizione_sinistra < dimensione_sinistra; posizione_sinistra++)
        sinistra_temp[posizione_sinistra] = vettore_di_numeri[indice_sinistra + posizione_sinistra];
    for (posizione_destra = 0; posizione_destra < dimensione_destra; posizione_destra++)
        destro_temp[posizione_destra] = vettore_di_numeri[indice_mezzo + 1 + posizione_destra];

    posizione_sinistra = 0;
    posizione_destra = 0;
    posizione_unita = indice_sinistra;

    /* Riunire le due metà nell'vettore originale */
    while (posizione_sinistra < dimensione_sinistra && posizione_destra < dimensione_destra)
    {
        if (sinistra_temp[posizione_sinistra] <= destro_temp[posizione_destra])
        {
            vettore_di_numeri[posizione_unita] = sinistra_temp[posizione_sinistra];
            posizione_sinistra++;
        }
        else
        {
            vettore_di_numeri[posizione_unita] = destro_temp[posizione_destra];
            posizione_destra++;
        }
        posizione_unita++;
    }

    while (posizione_sinistra < dimensione_sinistra)
    {
        vettore_di_numeri[posizione_unita] = sinistra_temp[posizione_sinistra];
        posizione_sinistra++;
        posizione_unita++;
    }
    while (posizione_destra < dimensione_destra)
    {
        vettore_di_numeri[posizione_unita] = destro_temp[posizione_destra];
        posizione_destra++;
        posizione_unita++;
    }

    free(sinistra_temp);
    free(destro_temp);
}

void ordinamento_per_fusione(int vettore_di_numeri[], int indice_sinistra, int indice_destro)
{
    if (indice_sinistra < indice_destro)
    {
        int indice_mezzo = indice_sinistra + (indice_destro - indice_sinistra) / 2;
        ordinamento_per_fusione(vettore_di_numeri, indice_sinistra, indice_mezzo);
        ordinamento_per_fusione(vettore_di_numeri, indice_mezzo + 1, indice_destro);
        fondi_sottoarray(vettore_di_numeri, indice_sinistra, indice_mezzo, indice_destro);
    }
}

int main()
{
    int numeri[] = {38, 27, 43, 3, 9, 82, 10};
    int lunghezza_vettore = 7;
    int indice;

    ordinamento_per_fusione(numeri, 0, lunghezza_vettore - 1);

    printf("vettore ordinata: ");
    for (indice = 0; indice < lunghezza_vettore; indice++)
        printf("%d ", numeri[indice]);
    printf("\n");
    return 0;
}
