#include <stdio.h>
#include <stdlib.h>

void mezclar_mitades(int arreglo_numerico[], int indice_izquierdo, int indice_medio, int indice_derecho)
{
    int tamanio_izquierdo = indice_medio - indice_izquierdo + 1;
    int tamanio_derecho = indice_derecho - indice_medio;
    int posicion_izquierda, posicion_derecha, posicion_combinada;

    int *temporal_izquierdo = (int *)malloc(tamanio_izquierdo * sizeof(int));
    int *temporal_derecho = (int *)malloc(tamanio_derecho * sizeof(int));

    /* copiar datos en arreglos temporales */
    for (posicion_izquierda = 0; posicion_izquierda < tamanio_izquierdo; posicion_izquierda++)
        temporal_izquierdo[posicion_izquierda] = arreglo_numerico[indice_izquierdo + posicion_izquierda];
    for (posicion_derecha = 0; posicion_derecha < tamanio_derecho; posicion_derecha++)
        temporal_derecho[posicion_derecha] = arreglo_numerico[indice_medio + 1 + posicion_derecha];

    posicion_izquierda = 0;
    posicion_derecha = 0;
    posicion_combinada = indice_izquierdo;

    /* mezclar las dos mitades de vuelta en el arreglo original */
    while (posicion_izquierda < tamanio_izquierdo && posicion_derecha < tamanio_derecho)
    {
        if (temporal_izquierdo[posicion_izquierda] <= temporal_derecho[posicion_derecha])
        {
            arreglo_numerico[posicion_combinada] = temporal_izquierdo[posicion_izquierda];
            posicion_izquierda++;
        }
        else
        {
            arreglo_numerico[posicion_combinada] = temporal_derecho[posicion_derecha];
            posicion_derecha++;
        }
        posicion_combinada++;
    }

    while (posicion_izquierda < tamanio_izquierdo)
    {
        arreglo_numerico[posicion_combinada] = temporal_izquierdo[posicion_izquierda];
        posicion_izquierda++;
        posicion_combinada++;
    }
    while (posicion_derecha < tamanio_derecho)
    {
        arreglo_numerico[posicion_combinada] = temporal_derecho[posicion_derecha];
        posicion_derecha++;
        posicion_combinada++;
    }

    free(temporal_izquierdo);
    free(temporal_derecho);
}

void ordenamiento_mezcla(int arreglo_numerico[], int indice_izquierdo, int indice_derecho)
{
    if (indice_izquierdo < indice_derecho)
    {
        int indice_medio = indice_izquierdo + (indice_derecho - indice_izquierdo) / 2;
        ordenamiento_mezcla(arreglo_numerico, indice_izquierdo, indice_medio);
        ordenamiento_mezcla(arreglo_numerico, indice_medio + 1, indice_derecho);
        mezclar_mitades(arreglo_numerico, indice_izquierdo, indice_medio, indice_derecho);
    }
}

int main()
{
    int numeros[] = {38, 27, 43, 3, 9, 82, 10};
    int longitud_arreglo = 7;
    int indice;

    ordenamiento_mezcla(numeros, 0, longitud_arreglo - 1);

    printf("Arreglo ordenado: ");
    for (indice = 0; indice < longitud_arreglo; indice++)
        printf("%d ", numeros[indice]);
    printf("\n");
    return 0;
}
