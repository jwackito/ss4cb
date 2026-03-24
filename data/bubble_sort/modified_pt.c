#include <stdio.h>

void bubble_sort(int array_de_numeros[], int tamanho_array)
{
    /* ordenar array_de_numeros em ordem crescente usando o algoritmo de ordenação por bolha */
    int passagem_externa;
    int passagem_interna;
    int valor_temporario;
    int houve_troca;

    for (passagem_externa = 0; passagem_externa < tamanho_array - 1; passagem_externa++)
    {
        houve_troca = 0;
        for (passagem_interna = 0; passagem_interna < tamanho_array - passagem_externa - 1; passagem_interna++)
        {
            if (array_de_numeros[passagem_interna] > array_de_numeros[passagem_interna + 1])
            {
                /* trocar elementos adjacentes  */
                valor_temporario = array_de_numeros[passagem_interna];
                array_de_numeros[passagem_interna] = array_de_numeros[passagem_interna + 1];
                array_de_numeros[passagem_interna + 1] = valor_temporario;
                houve_troca = 1;
            }
        }
        /* Se nenhum nenhuma ocorreu nesta passagem, o array já está ordenado. */
        if (houve_troca == 0)
            break;
    }
}

int main()
{
    int numeros[] = {64, 34, 25, 12, 22, 11, 90};
    int tamanho_array = 7;
    int indice;

    bubble_sort(numeros, tamanho_array);

    printf("Array ordenado: ");
    for (indice = 0; indice < tamanho_array; indice++)
    {
        printf("%d ", numeros[indice]);
    }
    printf("\n");
    return 0;
}
