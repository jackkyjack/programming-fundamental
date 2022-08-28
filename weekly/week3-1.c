#include <stdio.h>

int main()
{
    int n,m;
    printf("Enter number of rows to show star pattern : ");
    scanf("%d",&n);
    m=n-1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            for (int k = m; k > i; k--)
            {
                 printf("* ");
            }
        }
        printf("\n");
    }
    
    return 0;
}