#include <stdio.h>
#include <string.h>

int main()
{
    int num = 0,yai=65,lek=97;
    char text[100],*p;
    scanf("%s", text);
    for (int j = 0; j < 26; j++)
    {
        for (int i=0; i < strlen(text); i++)
        {
            if (text[i] == yai+j || text[i] == lek+j)
            {
                num++;
            }
        }
        printf("%c : %d\n", yai+j, num);
        num=0;
    }
    return 0;
}

//108