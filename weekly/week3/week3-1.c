#include <stdio.h>

int main()
{
    int n,m=1;
    printf("Enter number of rows to show star pattern : ");
    scanf("%d",&n);
    for (int i = n; i >= 1; i--)
    {
        for (int j = 0; j < i; j++)
        {
            printf(" ");
        }
        for (int k = 0; k < m; k++)
        {
            printf("* ");
        }
        m++;
        printf("\n");
    }
    return 0;
}