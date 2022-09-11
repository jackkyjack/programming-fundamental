#include <stdio.h>
#include <windows.h>
#include <conio.h>

void draw_ship(int x, int y)
{   
    COORD c = { x, y };
    SetConsoleCursorPosition(
        GetStdHandle(STD_OUTPUT_HANDLE), c);
    printf(" <-0-> ");
}
void erase_ship(int x,int y)
{
    COORD c ={x,y};
    SetConsoleCursorPosition(
        GetStdHandle(STD_OUTPUT_HANDLE), c);
        printf("     ");
}
int main()
{
    char ch = ' ';
    int x = 38, y = 20;
    draw_ship(x,y);
    do
    
    {
        if (_kbhit())
        {
            ch = (_kbhit());
            if (x >= 1 && x <= 80)
            {
                if (ch == 'a')
                {
                    erase_ship(x + 1,y);
                    draw_ship(--x,y);
                }
                if (ch == 'd')
                {
                    erase_ship(x - 1,y);
                    draw_ship(++x,y);
                }
            }
            if (y >= 1 && y <= 30)
            {
                if (ch == 'w')
                {
                    erase_ship(x,y);
                    draw_ship(x,--y);
                }
                if (ch =='s')
                {
                    erase_ship(x,y);
                    draw_ship(x,++y);
                }
            }
            fflush(stdin);
        }
        Sleep(100);
    } while (ch != 'x');
    return 0;
}