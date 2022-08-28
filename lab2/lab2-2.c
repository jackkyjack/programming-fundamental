#include <stdio.h>

int main()
{
    int x, y;
    printf("Enter first number : ");
    scanf("%d", &x);
    printf("Enter second number : ");
    scanf("%d", &y);
    while (x != y)
    {
        if (x > y)
        {
            x -= y;
        }
        else
        {
            y -= x;
        }
    }
    printf("Greatest common divisor = ");
    printf("%d",x);
    printf("\nPress any key to continue . . .");
    return 0;
}