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
    int x = 100;
    scanf("%d", &x);
    if (isPrime(x)==1) printf("Prime Number.");
    else printf("Not Prime Number.");
    return 0;
}