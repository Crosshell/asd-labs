#include <stdio.h>

int main() {
    int T, j;
    int A[7][8] = {0, 4, 5, 6, 6, 7, 8, 9,
                   -5, -3, 0, 2, 3, 5, 6, 7,
                   -5, 2, 3, 4, 8, 8, 9, 9,
                   0, 1, 4, 5, 8, 9, 15, 16,
                   2, 3, 5, 5, 6, 6, 7, 9,
                   1, 2, 3, 4, 5, 7, 8, 8,
                   3, 3, 4, 5, 6, 8, 8, 9};


    printf("Array before sorting: \n");

    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 8; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    printf("\n");


    for (int c = 0; c < 7; c++) {
        for (int i = 1; i < 8; i++) {
            T = A[c][i];
            j = i;
            while (A[c][j - 1] < T && j > 0) {
                A[c][j] = A[c][j - 1];
                j = j - 1;
            }
            A[c][j] = T;
        }
    }
    printf("Array after sorting: \n");
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 8; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    return 0;
}