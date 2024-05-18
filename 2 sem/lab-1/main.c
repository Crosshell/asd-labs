#include <stdio.h>

double loop(double x, int n, double sum, double f) {
    if (n == 1) {
        sum = 1;
    }
    for (int i = 3; i <= n; i++) {
        f = -f * x * (3 * i - 7) / (3 * i - 3);
        sum += f;
    }
    return sum;
}

double down(double x, int n, double sum, double f, double i){
    if (n == 1) {
        sum = 1;
    }
    if (i <= n){
        f = -f * x * (3 * i - 7) / (3 * i - 3);
        sum += f;
        sum = down(x, n, sum, f, i+1);
    }
    return sum;
}


double back(double x, int n, double f, double *sum) {
    if (n == 2){
        f = -x / 3;
    } else if (n > 2) {
        f = -back(x, n - 1, 0, sum) * x * (3 * n - 7) / (3 * n - 3);
    }
    *sum += f;
    return f;
}
double back_wrapper(double x, int n) {
    double sum = 1;
    back(x, n, 0, &sum);
    return sum;
}

double mixed(double x, int n, double f, int i){
    if (n == 1){
        f = 1;
    }
    else if (n > 2){
        f = -f * x * (3 * i - 7) / (3 * i - 3);
        f += mixed(x, n - 1, f, i + 1);
    }
    else {
        f = 1 - x / 3;
    }
    return f;
}

int main() {
    double x;
    int n;

    printf("Enter x: ");
    scanf("%lf", &x);
    printf("Enter n: ");
    scanf("%d", &n);

    printf("Result of loop: %lf\n", loop(x, n, 1 - x / 3, -x / 3));
    printf("Result of down: %lf\n", down(x, n, 1 - x / 3, -x / 3, 3));
    printf("Result of back: %lf\n", back_wrapper(x, n));
    printf("Result of mixed: %lf\n", mixed(x, n, -x / 3, 3));
    return 0;
}