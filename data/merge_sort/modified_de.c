#include <stdio.h>
#include <stdlib.h>

void haelften_zusammenfügen(int zahlen_array[], int linker_index, int mittel_index, int rechts_index)
{
    int linke_groesse = mittel_index - linker_index + 1;
    int rechte_groesse = rechts_index - mittel_index;
    int linke_position, rechte_position, zusammengeführte_position;

    int *links_temporär = (int *)malloc(linke_groesse * sizeof(int));
    int *rechts_temporär = (int *)malloc(rechte_groesse * sizeof(int));

    /* Daten in temporäre Arrays kopieren */
    for (linke_position = 0; linke_position < linke_groesse; linke_position++)
        links_temporär[linke_position] = zahlen_array[linker_index + linke_position];
    for (rechte_position = 0; rechte_position < rechte_groesse; rechte_position++)
        rechts_temporär[rechte_position] = zahlen_array[mittel_index + 1 + rechte_position];

    linke_position = 0;
    rechte_position = 0;
    zusammengeführte_position = linker_index;

    /* Füge die beiden haelften wieder zum ursprünglichen Array zusammen. */
    while (linke_position < linke_groesse && rechte_position < rechte_groesse)
    {
        if (links_temporär[linke_position] <= rechts_temporär[rechte_position])
        {
            zahlen_array[zusammengeführte_position] = links_temporär[linke_position];
            linke_position++;
        }
        else
        {
            zahlen_array[zusammengeführte_position] = rechts_temporär[rechte_position];
            rechte_position++;
        }
        zusammengeführte_position++;
    }

    while (linke_position < linke_groesse)
    {
        zahlen_array[zusammengeführte_position] = links_temporär[linke_position];
        linke_position++;
        zusammengeführte_position++;
    }
    while (rechte_position < rechte_groesse)
    {
        zahlen_array[zusammengeführte_position] = rechts_temporär[rechte_position];
        rechte_position++;
        zusammengeführte_position++;
    }

    free(links_temporär);
    free(rechts_temporär);
}

void zusammenführen_sortieren(int zahlen_array[], int linker_index, int rechts_index)
{
    if (linker_index < rechts_index)
    {
        int mittel_index = linker_index + (rechts_index - linker_index) / 2;
        zusammenführen_sortieren(zahlen_array, linker_index, mittel_index);
        zusammenführen_sortieren(zahlen_array, mittel_index + 1, rechts_index);
        haelften_zusammenfügen(zahlen_array, linker_index, mittel_index, rechts_index);
    }
}

int main()
{
    int zahlen[] = {38, 27, 43, 3, 9, 82, 10};
    int array_länge = 7;
    int index;

    zusammenführen_Sortieren(zahlen, 0, array_länge - 1);

    printf("Sortiertes Array: ");
    for (index = 0; index < array_länge; index++)
        printf("%d ", zahlen[index]);
    printf("\n");
    return 0;
}
