#organiza as pastas de arquivos, movendo e renomeando
#fonte: https://www.youtube.com/watch?v=qbW6FRbaSl0
import os
import json
import time
import pandas as  pd

from watchdog.observers import  Observer
#pip install watchdog(se nao tiver)

from watchdog.events import FileSystemEventHandler




class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            print(new_destination)
            #os.rename(src, new_destination)
            


folder_to_track = '/Users/rqfreitas/Downloads'
folder_destination = '/Users/rqfreitas/Downloads'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



