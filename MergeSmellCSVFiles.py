import glob
import pandas as pd
import tkinter
from tkinter import filedialog
import os


def browsefile_path():
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)

    print("\nfile_path_variable = ", tempdir)
    return tempdir

def merge(address,saveAddress):
    # address=browsefile_path()
    os.chdir(address)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    print(combined_csv)
    #export to csv


    dirpath = saveAddress
    foldername = os.path.basename(dirpath)
    savedirectory=saveAddress+'/'+foldername+"_CombinedAll"+'/'
    if not os.path.exists(savedirectory):
        os.makedirs(savedirectory)

    name=all_filenames[0][0:-4]+"_CombinedAll.csv"

    combined_csv.to_csv( savedirectory+ name, index=False, encoding='utf-8-sig')

def readDirectories():
    address = browsefile_path()
    folders_list = os.listdir(address)
    for directory in folders_list:
        final_address=address+'\\'+directory
        merge(final_address,address)

readDirectories()