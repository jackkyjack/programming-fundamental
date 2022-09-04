#include <stdio.h>
int main()
{

    int a, i, n, average,sum;
    printf("Enter n: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter number%d: ", i + 1);
        scanf("%d", &a);
        sum += a;
    }
    average = sum / n;

    printf("Average = %d", average);

    return 0;
}