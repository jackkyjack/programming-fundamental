#include <stdio.h>

int main()
{
    int n,m=1;
    printf("Enter number of rows to show star pattern : ");
    scanf("%d",&n);
    int i=n,j=0,k=0;
    while (i>=1)
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
        i--;
        printf("\n");
    }
    
    return 0;
}