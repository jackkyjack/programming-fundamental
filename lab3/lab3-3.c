#include <stdio.h>

int main()
{
    int num;
    int bang = 1;
    int a = 1;
    scanf("%d", &num);
    for (int l = 0; l < num; l++)
    {
        bang += 1;
    }
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            printf("*");
        }
        for (int k = 0; k <= bang; k++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            if (j == num - 1)
            {
                printf(" ");
            }
            else
            {
                printf("*");
            }
        }
        bang -= 2;
        printf("\n");
    }
    for (int i = num - 1; i >= 1; i--)
    {
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        for (int k = 0; k < a; k++)
        {
            printf(" ");
        }
        a += 2;
        for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}