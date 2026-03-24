#include <stdio.h>
#include <stdlib.h>

void mesclar_metades(int vetor_numero[], int indice_esquerdo, int indice_medio, int indice_direito)
{
    int tamanho_esquerdo = indice_medio - indice_esquerdo + 1;
    int tamanho_certo = indice_direito - indice_medio;
    int posição_esquerda, posição_direita, posição_mesclada;

    int *temp_esquerda = (int *)malloc(tamanho_esquerdo * sizeof(int));
    int *temp_direita = (int *)malloc(tamanho_certo * sizeof(int));

    /* Copiar dados para vetores temporárias */
    for (posição_esquerda = 0; posição_esquerda < tamanho_esquerdo; posição_esquerda++)
        temp_esquerda[posição_esquerda] = vetor_numero[indice_esquerdo + posição_esquerda];
    for (posição_direita = 0; posição_direita < tamanho_certo; posição_direita++)
        temp_direita[posição_direita] = vetor_numero[indice_medio + 1 + posição_direita];

    posição_esquerda = 0;
    posição_direita = 0;
    posição_mesclada = indice_esquerdo;

    /* Combine as duas metades de volta na vetor original. */
    while (posição_esquerda < tamanho_esquerdo && posição_direita < tamanho_certo)
    {
        if (temp_esquerda[posição_esquerda] <= temp_direita[posição_direita])
        {
            vetor_numero[posição_mesclada] = temp_esquerda[posição_esquerda];
            posição_esquerda++;
        }
        else
        {
            vetor_numero[posição_mesclada] = temp_direita[posição_direita];
            posição_direita++;
        }
        posição_mesclada++;
    }

    while (posição_esquerda < tamanho_esquerdo)
    {
        vetor_numero[posição_mesclada] = temp_esquerda[posição_esquerda];
        posição_esquerda++;
        posição_mesclada++;
    }
    while (posição_direita < tamanho_certo)
    {
        vetor_numero[posição_mesclada] = temp_direita[posição_direita];
        posição_direita++;
        posição_mesclada++;
    }

    free(temp_esquerda);
    free(temp_direita);
}

void ordenar_merge(int vetor_numero[], int indice_esquerdo, int indice_direito)
{
    if (indice_esquerdo < indice_direito)
    {
        int indice_medio = indice_esquerdo + (indice_direito - indice_esquerdo) / 2;
        ordenar_merge(vetor_numero, indice_esquerdo, indice_medio);
        ordenar_merge(vetor_numero, indice_medio + 1, indice_direito);
        mesclar_metades(vetor_numero, indice_esquerdo, indice_medio, indice_direito);
    }
}

int main()
{
    int numeros[] = {38, 27, 43, 3, 9, 82, 10};
    int tamanho_do_vetor = 7;
    int indice;

    ordenar_merge(numeros, 0, tamanho_do_vetor - 1);

    printf("Vetor ordenada: ");
    for (indice = 0; indice < tamanho_do_vetor; indice++)
        printf("%d ", numeros[indice]);
    printf("\n");
    return 0;
}
