#include <stdio.h>

int main()
{
    int number;
    int i = 2;
    printf("Enter number :");
    scanf("%d", &number);
    printf("Factoring Result : ");
    while (i > 1)
    {
        if (number % i == 0)
        {
            number = number / i;
            printf("%d", i);
            if (number != 1)
            {
                printf(" x ");
            }
        }
        else
        {
            i += 1;
        }
    }
    printf("\nPress any key to continue . . .");

    return 0;
}