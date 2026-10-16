# FileScrambler

Purpose
This folder contains a file-scrambling proof-of-concept intended for controlled testing in a disposable VM only.

Files of interest
- file_scrambler.py — Python source that scans common user folders (Desktop, Downloads, Documents) for many file types and renames/moves matching files; includes logic to copy executables into the working directory or system folders.
- ICON_DANCE.* (.exe, .pdb, .obj, etc.) — compiled binary and build artifacts produced during development/testing.
- build/, dist/ — packaging/build artifacts (dist/ is expected to contain compiled output when built).
- file_scrambler.spec — packaging spec kept for reference.

What it does (high level, non-actionable)
- Scans Desktop, Downloads, and Documents for files with many common extensions (images, documents, archives, media, executables, etc.).
- Generates randomized file names and extensions and renames or moves files, sometimes swapping files between folders.
- Copies or creates additional executable files (the script contains logic to copy an executable into the working directory or system folders).
- Runs in a loop and performs repeated file operations, also moving the mouse cursor to random positions to create additional disruption.

Risks / Why this is dangerous
- Can irreversibly rename, move, or overwrite user files, causing data loss and significant recovery work.
- Copying or placing executables into system locations can change system behavior or persist unwanted programs.
- Continuous file operations may make snapshot/backup-based recovery slower or incomplete.

Warning — do not run outside a disposable VM
This program will modify user files and can cause data loss. Do not execute any files from this folder on a host you care about. If you must work with this code for research, do so only in a fully isolated, disposable VM snapshot with no network access and with backups you can restore immediately.

Recommendations for maintainers
- Remove compiled executables, debug symbols, and dist/ folders before publishing or sharing the repository publicly.
- Keep only the source and clearly documented warnings if you need to keep this for research.
- Consider replacing destructive behaviors with inert mocks or sample outputs if you need to demonstrate behavior without risk.
