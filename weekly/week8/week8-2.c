#include <stdio.h>

int n, i;
unsigned long long fact = 1;

int factt(){
        for (i = 1; i <= n; ++i) {
            fact *= i;
        }
    }

int main() {
    
    printf("Enter an integer: ");
    scanf("%d", &n);

    if (n < 0)
        printf("Error!");
    else {
        factt();
        printf("Factorial of %d = %llu", n, fact);
    }

    return 0;
}