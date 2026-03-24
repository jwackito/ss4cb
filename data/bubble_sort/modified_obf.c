#include <stdio.h>

void f(int a[], int n) {
    int i, j, t, s;
    for (i = 0; i < n - 1; i++) {
        s = 0;
        for (j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
                s = 1;
            }
        }
        if (s == 0) break;
    }
}

int main() {
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7, i;
    f(a, n);
    for (i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
