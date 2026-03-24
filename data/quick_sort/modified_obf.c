#include <stdio.h>

void sw(int *a, int *b) { int t = *a; *a = *b; *b = t; }

int pt(int a[], int l, int h) {
    int pv = a[h], si = l - 1, i;
    for (i = l; i < h; i++)
        if (a[i] <= pv) { si++; sw(&a[si], &a[i]); }
    sw(&a[si + 1], &a[h]);
    return si + 1;
}

void qs(int a[], int l, int h) {
    if (l < h) {
        int pi = pt(a, l, h);
        qs(a, l, pi - 1);
        qs(a, pi + 1, h);
    }
}

int main() {
    int a[] = {10, 7, 8, 9, 1, 5};
    int n = 6, i;
    qs(a, 0, n - 1);
    for (i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
