#organiza as pastas de arquivos, movendo e renomeando
#fonte: https://www.youtube.com/watch?v=qbW6FRbaSl0
import os
import sys
import json
import time

import pandas as pd

from watchdog.observers import  Observer
#pip install watchdog(se nao tiver)

from watchdog.events import FileSystemEventHandler

df = pd.read_csv ('filesext.csv')
print(df)
mime = pd.DataFrame()
#sys.exit()

#pega a extensao

#Checa o tipo
#checa se ja existe a pasta, se nao, cria a pasta
#destEnd = folder_destination + foldExt
#if not os.path.isdir(MYDIR):
 #   os.makedirs(MYDIR)
 #   print("created folder : ", MYDIR)

#atribui folder_destination

folder_to_track = '/Users/rodrigofreitas/Downloads'
folder_destination = '/Users/rodrigofreitas/Downloads/forg'
i = 1
for filename in os.listdir(folder_to_track):
    #pega extensao
    lfilext = filename.split('.')
    filext = lfilext[-1]
    #print(filext)
    componto = "." + filext
    #checa tipo de midia
    mime = df.loc[df.Extension == componto,'mime']

    if mime.empty:
        print("vazio")
    else:
        #checa se ja existe a pasta, se nao, cria a pasta
        print(mime.values[0])
        destEnd = folder_destination + "/" + mime.values[0]
        if not os.path.isdir(destEnd):
            os.makedirs(destEnd)
            print("created folder : ", destEnd)
            #print(mime.values[0])
        src = folder_to_track + "/" + filename
        new_destination = destEnd + "/" + filename
            #print(new_destination)
        os.rename(src, new_destination)

    
            









