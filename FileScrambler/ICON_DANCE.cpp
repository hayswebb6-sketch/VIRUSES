#include <windows.h>
#include <commctrl.h>
#include <random>
#include <iostream>

#pragma comment(lib, "User32.lib")

void icon_dance(HWND hwnd, int iconIndex) {
    POINT iconPos{};
    LRESULT result=SendMessage(hwnd, LVM_GETITEMPOSITION, (WPARAM)iconIndex, (LPARAM)&iconPos); 

}
void performIconDance(HWND hwnd) {
    int iconCount = SendMessage(hwnd, LVM_GETITEMCOUNT, 0, 0);
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> disX(0, GetSystemMetrics(SM_CXSCREEN) - 1);
    std::uniform_int_distribution<> disY(0, GetSystemMetrics(SM_CYSCREEN) - 1);

    for (int i = 0; i < iconCount; ++i) {
        POINT iconPos{};
        SendMessage(hwnd, LVM_GETITEMPOSITION, (WPARAM)i, (LPARAM)&iconPos);

        int newX = disX(gen);
        int newY = disY(gen);

        SendMessage(hwnd, LVM_SETITEMPOSITION, (WPARAM)i, MAKELPARAM(newX, newY));
    }
}
int main() {
    return 0;
}
