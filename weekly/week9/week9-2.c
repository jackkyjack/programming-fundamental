#include <stdio.h>
#include <string.h>
int main()
{
    FILE *a;
    char s[10000];
    int x = 0;int i=0;
    a = fopen("C:\\code\\project\\profun\\data.txt", "w+");
    printf("Input data string:\n");
    while (1)
    {   scanf("%s", s);
        for(i = 0;i<strlen(s);i++){
            putc(s[i],a);
        }
        fprintf(a, "\n");
        x=strlen(s)-1;
        if (s[x] == '.')
        {
            break;
        }
    }
    fclose(a);
    return 0;
}