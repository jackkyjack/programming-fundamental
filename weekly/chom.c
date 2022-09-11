#include <stdio.h>
int main()
{
    int num1, num2, num3, x, y, z;
    printf("num1 :");
    scanf("%d", &num1);
    printf("num2 :");
    scanf("%d", &num2);
    printf("num3 :");
    scanf("%d", &num3);
    x = num1 + num2;
    y = num2 + num3;
    z = num1 + num3;

        
    if (x > y > z)
    {
        printf("%d", x);
    }
    if (y > x > z)
    {
        printf("%d", y);
    }
    if (z > x > y)
    {
        printf("%d", z);
    }

    return 0;
}