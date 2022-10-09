#include <stdio.h>
#include <windows.h>
#include <conio.h>
void draw_bullet(int, int);
void draw_ship(int, int);
void erase_bullet(int, int);
void erase_ship(int, int);
void setcursor(boolean);
void setcolor(int, int);
void gotoxy(int, int);

int main()
{
    char ch = ' ';
    setcursor(0);
    setcolor(2, 4);
    int bulletArray[5][3] = { {-1, -1, 0}, {-1, -1, 0}, {-1, -1, 0}, {-1, -1, 0}, {-1, -1, 0} }, b = 0;
    int x = 40, y = 20;
    int bullet = 5;
    int moveLeft = 0, moveRight = 0;
    draw_ship(x, y);
    do
    {
        if (_kbhit())
        {
            ch = _getch();
            if (ch == 'a' && x != 0)
            {
                moveLeft = 1;
                moveRight = 0;
            }
            if (ch == 'd' && x != 76)
            {
                moveLeft = 0;
                moveRight = 1;
            }
            if (ch == 's')
            {
                moveLeft = 0;
                moveRight = 0;
            }
            if (ch == ' ' && bullet > 0)
            {
                bulletArray[b][0] = x + 2;
                bulletArray[b][1] = y - 1;
                bulletArray[b][2] = 1;
                draw_bullet(bulletArray[b][0], bulletArray[b][1]);
                b++;
                b = b % 5;
                bullet--;
                
            }

            fflush(stdin);
        }
        if (moveLeft == 1 && x != 0)
        {
            erase_ship(x, y);
            draw_ship(--x, y);
        }
        if (moveRight == 1 && x != 76)
        {
            erase_ship(x, y);
            draw_ship(++x, y);
        }
        for (int i = 0; i < 5; i++)
        {
            if (bulletArray[i][2] == 1)
            {
                erase_bullet(bulletArray[i][0], bulletArray[i][1]);
                if (bulletArray[i][1] == 0)
                {
                    bulletArray[i][2] = 0;
                    bullet++;
                }
                else
                {
                    draw_bullet(bulletArray[i][0], --bulletArray[i][1]);
                }
            }
        }
        Sleep(50);
    } while (ch != 'x');
    return 0;
}

void gotoxy(int x, int y) {
    COORD c = { x, y };
    SetConsoleCursorPosition(
        GetStdHandle(STD_OUTPUT_HANDLE), c);
}
void draw_ship(int x, int y)
{
    gotoxy(x, y);
    setcolor(2, 4);
    printf("<-0->");
}

void draw_bullet(int x, int y)
{
    gotoxy(x, y);
    setcolor(7, 0);
    printf(".");
}

void erase_ship(int x, int y)
{
    gotoxy(x, y);
    setcolor(0, 0);
    printf("     ");
}

void erase_bullet(int x, int y)
{
    gotoxy(x, y);
    setcolor(0, 0);
    printf(" ");
}

void setcursor(boolean visible)
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