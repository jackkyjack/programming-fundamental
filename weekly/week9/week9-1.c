#include <stdio.h>
#include <string.h>
int main()
{
    FILE *a;
    char s[10000];
    int x = 0;
    a = fopen("C:\\code\\project\\profun\\data.txt", "w+");
    printf("Input data string:\n");
    while (1)
    {
        scanf("%s", s);
        x=strlen(s)-1;
        fprintf(a, s);
        fprintf(a, "\n");
        if (s[x] == '.')
        {
            break;
        }
    }
    fclose(a);
    return 0;
}

//66