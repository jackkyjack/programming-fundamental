#include <stdio.h>

int main()
{
    int x, i, j;
    printf("Enter number : ");
    scanf("%d", &x);
    for (i = 1; i <= x; i++)
    {
        for (j = 1; j <= x; j++)
        {
            if (j == 1 || j == x || i == 1 || i == x)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("\nPress any key to continue . . .");
    return 0;
}