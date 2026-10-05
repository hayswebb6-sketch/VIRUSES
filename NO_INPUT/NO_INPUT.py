import tkinter as tk
import ctypes
import os
import PIL.Image, PIL.ImageTk
background=PIL.ImageTk.PhotoImage(PIL.Image.open("NO_INPUT.jpeg"))

def change_wallpaper(image_path):
    image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
root=tk.Tk()
label=tk.Label(root, image=background)
label.pack(fill="both", expand=True)
root.attributes("-alpha", 0.0)
root.overrideredirect(True)
ctypes.windll.user32.BlockInput(True)
change_wallpaper("NO_INPUT.jpeg")
root.mainloop()