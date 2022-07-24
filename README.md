# AutoSort
Simple auto sorting program which allows the user to specify a directory to be sorted. Change top lines to set your destination folders as well as which extension goes where. Uses watchdog to monitor folder and os to move files, tkinter is used for the GUI

This Program will not work if you do not specify paths for each category of file. IF there is a section which you do not need simply comment out the directory line and the coorosponding function. Ex: if you don't use torrents comment out line 46: torrent_extensions as well as line 129-133: check_torrent_files.

Updated to automatically remove SortIsRunning.txt and re-create it if it alreayd exists in the directory. (This is caused by exitiing the program by closing the shell rather than keyboard interupt (ctrl + c) 
