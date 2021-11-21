from more_itertools import unique_everseen
import tkinter as tk
from tkinter import filedialog
import csv
import os


def browsefile_path():
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames()
    return files[0]

def readcsvsmellfile(address):
    with open(address, 'r') as file:
        reader = csv.reader(file)
        listcsvsmellfile=list()
        for row in reader:
            listcsvsmellfile.append(row)
        return listcsvsmellfile


def cleanDuplicates(source,dest):
    with open(source,'r') as f, open(dest,'w') as out_file:
        out_file.writelines(unique_everseen(f))

def cleanNoneItems():
    address=browsefile_path()
    listcsvsmellfile = readcsvsmellfile(address)

    removecandidatelist=list()
    for entity in listcsvsmellfile:
        if entity.count('') > 10 or entity.count('0') > 10:
            removecandidatelist.append(entity)

    for candidate in removecandidatelist:
        listcsvsmellfile.remove(candidate)

    with open(address[:-7]+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(listcsvsmellfile)

def cleandup():
    address=browsefile_path()
    source=address
    dest=address[:-4]+'_CleanedDup.csv'
    cleanDuplicates(source,dest)

def clean():
    cleanNoneItems()

while(True):
    clean()