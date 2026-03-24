#include <stdio.h>

void bubble_sort(int zahl_array[], int array_laenge)
{
    /* Sortiere das Array zahl_array mithilfe des Bubble-Sort-Verfahrens in aufsteigender Reihenfolge. */
    int äußerer_durchgang;
    int innerer_durchgang;
    int temporärer_wert;
    int vertauscht;

    for (äußerer_durchgang = 0; äußerer_durchgang < array_laenge - 1; äußerer_durchgang++)
    {
        vertauscht = 0;
        for (innerer_durchgang = 0; innerer_durchgang < array_laenge - äußerer_durchgang - 1; innerer_durchgang++)
        {
            if (zahl_array[innerer_durchgang] > zahl_array[innerer_durchgang + 1])
            {
                /* vertausche benachbarte elemente */
                temporärer_wert = zahl_array[innerer_durchgang];
                zahl_array[innerer_durchgang] = zahl_array[innerer_durchgang + 1];
                zahl_array[innerer_durchgang + 1] = temporärer_wert;
                vertauscht = 1;
            }
        }
        /* Falls in diesem Durchgang kein Tauschvorgang stattfand, ist das Array bereits sortiert. */
        if (vertauscht == 0)
            break;
    }
}

int main()
{
    int zahlen[] = {64, 34, 25, 12, 22, 11, 90};
    int array_laenge = 7;
    int index;

    bubble_sort(zahlen, array_laenge);

    printf("Sorted array: ");
    for (index = 0; index < array_laenge; index++)
    {
        printf("%d ", zahlen[index]);
    }
    printf("\n");
    return 0;
}
