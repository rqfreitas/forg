#organiza as pastas de arquivos, movendo e renomeando
#fonte: https://www.youtube.com/watch?v=qbW6FRbaSl0
import os
import sys
import json
import time
import pandas as pd


df = pd.read_csv ('filesext.csv')
mime = pd.DataFrame()


def forg():
    folder_to_track = os.getcwd() #'/Users/rodrigofreitas/Downloads'
    folder_destination = folder_to_track + "/forg"


    #CREATE PASTA FORG IF IT DOESN'T EXISTS
    if not os.path.isdir(folder_to_track + "/forg"):
        os.makedirs(folder_to_track + "/forg")

    i = 1

    for filename in os.listdir(folder_to_track):

        #pega extensao
        lfilext = filename.split('.')
        filext = lfilext[-1]
        componto = "." + filext.lower()

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

    
            

def main():
    forg()

if __name__ == "__main__":
    main()





