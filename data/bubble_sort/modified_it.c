#include <stdio.h>

void bubble_sort(int vettore_numeri[], int lunghezza_vettore)
{
    /* Ordina vettore_numeri in ordine crescente utilizzando il bubble sort */
    int iterazione_esterno;
    int iterazione_interno;
    int valore_temporaneo;
    int scambiato;

    for (iterazione_esterno = 0; iterazione_esterno < lunghezza_vettore - 1; iterazione_esterno++)
    {
        scambiato = 0;
        for (iterazione_interno = 0; iterazione_interno < lunghezza_vettore - iterazione_esterno - 1; iterazione_interno++)
        {
            if (vettore_numeri[iterazione_interno] > vettore_numeri[iterazione_interno + 1])
            {
                /* scambio di elementi adiacenti */
                valore_temporaneo = vettore_numeri[iterazione_interno];
                vettore_numeri[iterazione_interno] = vettore_numeri[iterazione_interno + 1];
                vettore_numeri[iterazione_interno + 1] = valore_temporaneo;
                scambiato = 1;
            }
        }
        /* Se in questo iterazione non si è verificato alcuno scambio, l'vettore è già ordinato. */
        if (scambiato == 0)
            break;
    }
}

int main()
{
    int numeri[] = {64, 34, 25, 12, 22, 11, 90};
    int lunghezza_vettore = 7;
    int indice;

    bubble_sort(numeri, lunghezza_vettore);

    printf("vettore ordinato: ");
    for (indice = 0; indice < lunghezza_vettore; indice++)
    {
        printf("%d ", numeri[indice]);
    }
    printf("\n");
    return 0;
}
