#include <stdio.h>

void elementi_di_scambio(int *primo_elemento, int *secondo_elemento)
{
    int valore_temporaneo = *primo_elemento;
    *primo_elemento = *secondo_elemento;
    *secondo_elemento = valore_temporaneo;
}

int array_di_partizione(int array_di_numeri[], int indice_basso, int indice_alto)
{
    int valore_pivot = array_di_numeri[indice_alto];
    int indice_elemento_piu_piccolo = indice_basso - 1;
    int indice_attuale;

    for (indice_attuale = indice_basso; indice_attuale < indice_alto; indice_attuale++)
    {
        if (array_di_numeri[indice_attuale] <= valore_pivot)
        {
            indice_elemento_piu_piccolo++;
            elementi_di_scambio(&array_di_numeri[indice_elemento_piu_piccolo], &array_di_numeri[indice_attuale]);
        }
    }
    elementi_di_scambio(&array_di_numeri[indice_elemento_piu_piccolo + 1], &array_di_numeri[indice_alto]);
    return indice_elemento_piu_piccolo + 1;
}

void ordinamento_rapido(int array_di_numeri[], int indice_basso, int indice_alto)
{
    if (indice_basso < indice_alto)
    {
        int pivot_indice = array_di_partizione(array_di_numeri, indice_basso, indice_alto);
        ordinamento_rapido(array_di_numeri, indice_basso, pivot_indice - 1);
        ordinamento_rapido(array_di_numeri, pivot_indice + 1, indice_alto);
    }
}

int main()
{
    int numeri[] = {10, 7, 8, 9, 1, 5};
    int lunghezza_array = 6;
    int indice;

    ordinamento_rapido(numeri, 0, lunghezza_array - 1);

    printf("Array ordinata: ");
    for (indice = 0; indice < lunghezza_array; indice++)
        printf("%d ", numeri[indice]);
    printf("\n");
    return 0;
}
