#include <stdio.h>

void tausch_elemente(int *erstes_element, int *zweites_element)
{
    int temp_wert = *erstes_element;
    *erstes_element = *zweites_element;
    *zweites_element = temp_wert;
}

int partitioniere_array(int zahlen_array[], int rechts, int hoher_index)
{
    int pivot_Wert = zahlen_array[hoher_index];
    int kleiner_index = rechts - 1;
    int aktueller_index;

    for (aktueller_index = rechts; aktueller_index < hoher_index; aktueller_index++)
    {
        if (zahlen_array[aktueller_index] <= pivot_Wert)
        {
            kleiner_index++;
            tausch_elemente(&zahlen_array[kleiner_index], &zahlen_array[aktueller_index]);
        }
    }
    tausch_elemente(&zahlen_array[kleiner_index + 1], &zahlen_array[hoher_index]);
    return kleiner_index + 1;
}

void quicksort_implementierung(int zahlen_array[], int rechts, int hoher_index)
{
    if (rechts < hoher_index)
    {
        int pivot_index = partition_array(zahlen_array, rechts, hoher_index);
        quicksort_implementierung(zahlen_array, rechts, pivot_index - 1);
        quicksort_implementierung(zahlen_array, pivot_index + 1, hoher_index);
    }
}

int main()
{
    int zahlen[] = {10, 7, 8, 9, 1, 5};
    int array_groesse = 6;
    int index;

    quicksort_implementierung(zahlen, 0, array_groesse - 1);

    printf("Sortiertes array: ");
    for (index = 0; index < array_groesse; index++)
        printf("%d ", zahlen[index]);
    printf("\n");
    return 0;
}
