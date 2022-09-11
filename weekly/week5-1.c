#include <stdio.h>

int isPrime(int p)
{
    int a=2;
    while (p!=a)
    {
        if (p % a!=0) a++;
        else return 0;
    }
    return 1;
}
int main()
{
    int x;
    printf("Enter a positive integer: ");
    scanf("%d", &x);
    if (isPrime(x)==1) printf("%d is a Prime Number.",x);
    else printf("%d is not a Prime Number.",x);
    return 0;
}