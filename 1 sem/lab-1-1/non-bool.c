#include <stdio.h>

int main() {

    float x,y;
    printf("Input x:\n");
    scanf("%f", &x);

    if(x > 0){
        if(x <= 5){
            y = x * x * x - 5 * x * x;
            printf("Output y = %f", y);
        }
        else if(x > 10){
            y = x * x - 3;
            printf("Output y = %f", y);
        }
        else{
            printf("x does not in interval: [-32,-20) U (0,5] U (10, +inf)");
        }
    }
    else if(x < -20){
        if(x >= -32){
            y = x * x - 3;
            printf("Output y = %f", y);
        }
        else{
            printf("x does not in interval: [-32,-20) U (0,5] U (10, +inf)");
        }
    }
    else{
        printf("x does not in interval: [-32,-20) U (0,5] U (10, +inf)");
    }

    return 0;
}