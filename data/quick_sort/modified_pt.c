#include <stdio.h>

void trocar_elementos(int *primeiro_elemento, int *segundo_elemento)
{
    int valor_temporario = *primeiro_elemento;
    *primeiro_elemento = *segundo_elemento;
    *segundo_elemento = valor_temporario;
}

int particionar_vetor(int vetor_numero[], int indice_baixo, int indice_alto)
{
    int valor_pivot = vetor_numero[indice_alto];
    int indice_de_elemento_menor = indice_baixo - 1;
    int indice_atual;

    for (indice_atual = indice_baixo; indice_atual < indice_alto; indice_atual++)
    {
        if (vetor_numero[indice_atual] <= valor_pivot)
        {
            indice_de_elemento_menor++;
            trocar_elementos(&vetor_numero[indice_de_elemento_menor], &vetor_numero[indice_atual]);
        }
    }
    trocar_elementos(&vetor_numero[indice_de_elemento_menor + 1], &vetor_numero[indice_alto]);
    return indice_de_elemento_menor + 1;
}

void ordenacao_rapida(int vetor_numero[], int indice_baixo, int indice_alto)
{
    if (indice_baixo < indice_alto)
    {
        int indice_pivot = particionar_vetor(vetor_numero, indice_baixo, indice_alto);
        ordenacao_rapida(vetor_numero, indice_baixo, indice_pivot - 1);
        ordenacao_rapida(vetor_numero, indice_pivot + 1, indice_alto);
    }
}

int main()
{
    int numeros[] = {10, 7, 8, 9, 1, 5};
    int tamanho_do_vetor = 6;
    int indice;

    ordenacao_rapida(numeros, 0, tamanho_do_vetor - 1);

    printf("vetor ordenada: ");
    for (indice = 0; indice < tamanho_do_vetor; indice++)
        printf("%d ", numeros[indice]);
    printf("\n");
    return 0;
}
