#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
int main()
{
    struct player
    {
        char name[50];
        int level;
        int score;
    };

    struct player p[5], *ptr;
    for (int i = 0; i < 5; i++)
    {
        scanf("%s", p[i].name);
        scanf("%d", &p[i].level);
        scanf("%d", &p[i].score);
    }
    ptr = p;

    FILE* fp;
    fp = fopen("mytestfile.txt", "w");
    for (int i = 0; i < 5; i++)
    {
        fprintf(fp, "%s %d %d \n", ptr->name, ptr->level, ptr->score);
        ptr++;
    }
    fclose(fp);
    return 0;
}