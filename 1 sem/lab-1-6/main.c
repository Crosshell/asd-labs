#include <stdio.h>
#include <windows.h>

int main() {
    HANDLE hout = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD Pos;
    int i, j, sum;
    int h = 24;
    int w = 80;
    for (sum = h+w-2; sum >= 0; sum--) {
        if (sum % 2 == 0) {
            for (j = w-1; j >= 0; j--) {
                for (i = 0; i <= h - 1; i++) {
                    if (sum == i + j) {
                        Pos.X = j;
                        Pos.Y = i;
                        SetConsoleCursorPosition(hout, Pos);
                        printf("#");
                        Sleep(5);
                    }
                }
            }
        } else {
            for (i = h-1; i >= 0; i--) {
                for (j = 0; j <= w-1; j++) {
                    if (sum == i + j) {
                        Pos.X = sum-i;
                        Pos.Y = i;
                        SetConsoleCursorPosition(hout, Pos);
                        printf("#");
                        Sleep(5);
                    }
                }
            }
        }
    }
    getchar();
    return 0;
}
