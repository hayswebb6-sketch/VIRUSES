# ENDLESS_BSOD

Purpose
This folder contains a Windows-targeted proof-of-concept that displays a fullscreen BSOD-style screen and attempts to persist/lock the UI. It is intended for controlled testing in a disposable virtual machine only.

Files of interest
- Endless_BSOD.py — Python source that displays a fullscreen image, attempts to hide the taskbar/cursor, set the wallpaper, block input where possible, and add itself to startup.
- red_bsod.png — image used as the fullscreen display and wallpaper.
- build/, dist/ — packaging/build artifacts (dist/ is expected to contain ENDLESS_BSOD.exe after building).
- ENDLESS_BSOD.spec — PyInstaller (or similar) spec file kept for packaging reference.

Behavior (high level)
- Shows a fullscreen window using tkinter and Pillow (PIL) sized to the screen resolution.
- Attempts to change the desktop wallpaper to the included image and repeatedly keep the window focused.
- Attempts to hide the taskbar and continuously hide the cursor; tries to block input via ctypes where permitted.
- Attempts to add a shortcut to the Windows Startup folder to persist across reboots.

Security & safety (do not run)
This code is intentionally disruptive. Running it on a host you care about may result in a system that is difficult to interact with (fullscreen takeover, hidden taskbar/cursor, blocked input). Do not execute any files from this folder outside of a disposable VM snapshot that can be reverted. Do not share compiled binaries unless you clearly disclose they are harmful.

Notes for repository maintainers
- Keep only source in public copies when possible; remove dist/ and compiled executables before publishing.
- Add explicit VM/sandbox testing instructions and a clear, prominent warning in the top-level README.
