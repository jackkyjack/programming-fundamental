#include <stdio.h>

int num ;

int fact(int y)
{

    if (y == 0)

        return 1;

    return y * fact(y - 1);
}

int main()
{
    printf("Enter an integer: ");
    scanf("%d",&num);
    printf("Factorial of %d = %d",num, fact(num));
    return 0;
}

//45