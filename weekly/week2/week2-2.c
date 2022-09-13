#include <stdio.h>
#include <string.h>

int main()
{
    char str[1000];
    scanf("%s",&str);
    printf("%c",str[strlen(str)-1]);
    return 0;
}