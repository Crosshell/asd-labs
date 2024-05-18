#include <stdio.h>
#include <math.h>

int main() {
    int n, i, j, c_op;
    double product, sum;
    product = 1;
    c_op = 0;
    printf("Print n:\n");
    scanf("%d",&n);

    for(i = 1; i <= n; i++){
        sum = 0;
        for(j = 1; j<=i; j++){
            sum += j + sin(j);
            c_op += 7;
        }
        product *= ((i*i + 1) / sum);
        c_op += 9;

    }
    c_op += 3;
    printf("Result = %.7f\n", product);
    printf("Count of operation = %d", c_op);
    return 0;
}