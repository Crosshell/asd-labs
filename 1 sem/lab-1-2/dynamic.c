#include <stdio.h>
#include <math.h>

int main() {
    int n, i, c_op;
    double product, sum;
    product = 1;
    c_op = 0;
    printf("Print n:\n");
    scanf("%d",&n);

    for(i = 1; i <= n; i++){
        sum += i + sin(i);
        product *= ((i*i + 1) / sum);
        c_op += 11;
    }
    c_op += 3;
    printf("Result = %.7f\n", product);
    printf("Count of operation = %d", c_op);
    return 0;
}