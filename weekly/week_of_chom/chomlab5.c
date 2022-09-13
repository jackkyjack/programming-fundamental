#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <stdlib.h>

void draw_ship(int x, int y)
{

    COORD c = {x, y};
    SetConsoleCursorPosition(
        GetStdHandle(STD_OUTPUT_HANDLE), c);
    printf(" <-0-> ");
}
void setcursor(bool visible)
{
    HANDLE console = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO lpCursor;
    lpCursor.bVisible = visible;
    lpCursor.dwSize = 20;
    SetConsoleCursorInfo(console, &lpCursor);
}
void setcolor(int fg, int bg)
{
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, bg * 16 + fg);
}

int main()
{
    setcolor(4, 2);
    system("cls");
    char ch = ' ';
    int x = 38, y = 20;
    draw_ship(x, y);

    do
    {

        if (_kbhit())
        {
            ch = _getch();
            system("CLS");
            if (ch == 'a' && x > 0)
            {
                draw_ship(x -= 2, y);
            }
            else if (ch == 'w' && y > 0)
            {
                draw_ship(x, --y);
            }
            else if (ch == 's' && y < 30)
            {

                draw_ship(x, ++y);
            }
            else if (ch == 'd' && x < 80)
            {
                draw_ship(x += 2, y);
            }
            else
            {
                draw_ship(x, y);
            }
            fflush(stdin);
        }
        Sleep(100);
    } while (ch != 'x');
    return 0;
}