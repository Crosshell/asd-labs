#include <stdio.h>

int main(){
    int i, j, L, R, mid;
    double X;

    //Задання матриці та розміру

    int row = 7;
    int colm = 9;
    double matrix[7][9] = {9,8,7,5,7,8,9,5,0,
                        8,8, 7,3,4,6,9,4,-2,
                        8,8,6,2,2,4,7,1,-2,
                        7,3,6,2,2,4,7,0,-6,
                        4,3,5,1,1,2,5,0,-6,
                        3,2,4,0,1,1,3,-5,-82,
                        3,2,2,0,-3,0,2,-7,-9};

    //Виведення матриці

    for (i = 0; i < 7; i++) {
        for (j = 0; j < 9; j++) {
            printf("%.1f ", matrix[i][j]);
        }
        printf("\n");
    }

    //Введення числа "X"

    printf("Enter X:");
    scanf("%lf", &X);

    //Двійковий пошук

    for(i = 0; i < colm; i++){
        L = 0;
        R = row-1;
        while (L < R){
            mid = (L+R)/2;
            if(matrix[mid][i] > X){
                L = mid+1;
            }
            else{
                R = mid;
            }
        }

        //Результат

        if(matrix[R][i] == X){
            printf("X in column %d and row %d, [%d ; %d];\n",i,R,i,R);
        }
        else{
            printf("X not in column %d\n",i);
        }
    }
    getchar();
    return 0;
}