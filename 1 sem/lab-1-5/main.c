#include <stdio.h>

int main() {
    int i, j;
    double firstPositive, lastNegative;
    int firstPositiveid = -1, lastNegativeid = -1;
    double arr[7][7] = {  // Початкова матриця
            5, 4, -6, 2, 1, 8, -4,
            -4, 6, -9, -7, -3, 2, -5,
            -3, 9, 7, 6, -5, -6, 8,
            -7, 5, 1, 1, 5, 8, 4,
            -3, 2, 2, -4, 2, -7, 9,
            3, 1, 7, 8, -3, 3, 0,
            4, 4, 7, -5, 7, 5, 4


    };
    for (i = 0; i < 7; i++) {  //Виведення матриці
        for (j = 0; j < 7; j++) {
            printf("%.1f ", arr[i][j]);
        }
        printf("\n");
    }
    for (i = 0; i < 7; i++){ // Пошук першого додатнього
            if (arr[i][i] > 0){
                firstPositiveid = i;
                firstPositive = arr[i][i];
                break;
            }
    }
    for (i = 0; i < 7; i++){ //Пошук останнього мінусу
            if (arr[i][i] < 0){
                lastNegativeid = i;
                lastNegative = arr[i][i];
        }
    }
    if (firstPositiveid != -1 && lastNegativeid != -1) {
        arr[firstPositiveid][firstPositiveid] = lastNegative;
        arr[lastNegativeid][lastNegativeid] = firstPositive;
    }
    printf("Second Matrix:\n");
    for (i = 0; i < 7; i++) {  //Виведення матриці після операції
        for (j = 0; j < 7; j++) {
            printf("%.1f ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
