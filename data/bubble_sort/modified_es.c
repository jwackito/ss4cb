#include <stdio.h>

void ordenamiento_burbuja(int arreglo_numerico[], int longitud_arreglo)
{
    /* Ordena el arreglo_numerico en orden ascendente usando ordenamiento burbuja */
    int pasaje_externo;
    int pasaje_interno;
    int valor_temporal;
    int intercambiado;

    for (pasaje_externo = 0; pasaje_externo < longitud_arreglo - 1; pasaje_externo++)
    {
        intercambiado = 0;
        for (pasaje_interno = 0; pasaje_interno < longitud_arreglo - pasaje_externo - 1; pasaje_interno++)
        {
            if (arreglo_numerico[pasaje_interno] > arreglo_numerico[pasaje_interno + 1])
            {
                /* intercambio de elementos adyacentes*/
                valor_temporal = arreglo_numerico[pasaje_interno];
                arreglo_numerico[pasaje_interno] = arreglo_numerico[pasaje_interno + 1];
                arreglo_numerico[pasaje_interno + 1] = valor_temporal;
                intercambiado = 1;
            }
        }
        /* Si no ocurre un intercambio en este pasaje, el arreglo ya esta ordenado */
        if (intercambiado == 0)
            break;
    }
}

int main()
{
    int numero[] = {64, 34, 25, 12, 22, 11, 90};
    int longitud_arreglo = 7;
    int indice;

    ordenamiento_burbuja(numero, longitud_arreglo);

    printf("arreglo ordenado: ");
    for (indice = 0; indice < longitud_arreglo; indice++)
    {
        printf("%d ", numero[indice]);
    }
    printf("\n");
    return 0;
}
