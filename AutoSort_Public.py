from cgitb import text
from operator import truediv
from os import scandir, rename
from os.path import splitext, exists
from shutil import move
from time import sleep
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import *;
import tkinter as tkinter
from tkinter.ttk import *;

# ! FILL IN BELOW
# ? folder to track e.g. Windows: "C:/Users/user/Downloads"
source_dir = ""
dest_dir_sfx = ""
dest_dir_music = ""
dest_dir_video = ""
dest_dir_image = ""
dest_dir_documents = ""
dest_dir_programs = ""
dest_dir_archives = ""
dest_dir_codes = ""
dest_dir_torrents =""

# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt"]
# ? supported Program types
program_extensions = [".exe" , ".lnk" , ".url"]
# ? supported archive types
archive_extensions = [".rar" , ".zip", "7z"]
# ? supported Code types
code_extensions = [".js", ".py", ".scss", ".jsx", ".bin", ".config", ".batch", ".dll"]
# ? torrents'
torrent_extensions = [".torrent"]

def make_unique(path):
    filename, extension = splitext(path)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(path):
        path = f"{filename} ({counter}){extension}"
        counter += 1

    return path


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(name)
        rename(entry, unique_name)
    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    # ? THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # ? .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_program_files(entry, name)
                self.check_archive_files(entry, name)
                self.check_code_files(entry, name)
                self.check_torrent_files(entry, name)
                

    def check_audio_files(self, entry, name):  # * Checks all Audio Files
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # ? 10Megabytes
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # * Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # * Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # * Checks all Document Files
        for documents_extension in document_extensions:
            if (name.endswith(documents_extension) or name.endswith(documents_extension.upper())) and name != "SortIsRunning.txt":
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_program_files(self, entry, name):  # * Checks all Program Files
        for programs_extension in program_extensions:
            if name.endswith(programs_extension) or name.endswith(programs_extension.upper()):
                move_file(dest_dir_programs, entry, name)
                logging.info(f"Moved program file: {name}")

    def check_archive_files(self, entry, name): # * Checks all Archive Files
        for archive_extension in archive_extensions:
            if name.endswith(archive_extension) or name.endswith(archive_extension.upper()):
                move_file(dest_dir_archives, entry, name)
                logging.info(f"Moved Archive file: {name}")

    def check_code_files(self, entry, name): # * Checks all code Files
        for code_extension in code_extensions:
            if name.endswith(code_extension) or name.endswith(code_extension.upper()):
                move_file(dest_dir_codes, entry, name)
                logging.info(f"Moved code file: {name}")

    def check_torrent_files(self, entry, name): # * Checks all torrent Files
        for torrent_extension in torrent_extensions:
            if name.endswith(torrent_extension) or name.endswith(torrent_extension.upper()):
                move_file(dest_dir_torrents, entry, name)
                logging.info(f"Moved code file: {name}")

# GUI Window
master = tkinter.Tk()
master.geometry('465x150')
master.title('File Sort')
master.configure(bg='grey')

# Welcome message
msg = tkinter.Label (master, text= " Welcome to AutoSort, specify a directory and click run to enable sorting for said folder")
msg.grid(column=0, row=0)

#Directory input
inputtxt = Text(master, height=3, width=50 )
inputtxt.insert('1.0', "Enter Directory path here (delete this text)")
inputtxt.grid(column=0, row=1)

#Set Directory
def setDir(): 
    inp = inputtxt.get(1.0, "end-1c")
    global source_dir
    source_dir = inp
    lbl.config(text= "Selected Directory: "+inp)


#Run Sort
def runSort():
    print (("*\n")*3 +"Directory:" + source_dir + ". Destroying master")
    master.destroy()
    
    

#Button creation
setButton = tkinter.Button(master, text = "Set Directory", command= setDir)
setButton.grid(column=0, row=2)


runButton = tkinter.Button(master, text = "Run", command= runSort )
runButton.grid(column=0, row = 3)

#Label creation
lbl = tkinter.Label(master, text='')
lbl.grid(column=0, row=4)






# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    
    #tkinter GUI window
    master.mainloop()

    #Watchdog Observer loop
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    # Create Temp txt file to update observer. Remove and create again if eixst already
    try:
        os.remove(source_dir + "/SortIsRunning.txt")
        rs = open(source_dir + "/SortIsRunning.txt", 'w')
        rs.close()
    except:
        rs = open(source_dir + "/SortIsRunning.txt", 'w')
        rs.close()

    #Console text
    print(("*\n")*3 +"Auto Sort is active in " + source_dir + 
    ". Use control C or close this window to end program"
    )
    
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        os.remove(source_dir + "/SortIsRunning.txt")
        observer.stop()
    observer.join()

