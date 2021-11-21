import glob
import tkinter
from tkinter import filedialog
import os
import shutil


def browsefile_path():
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)

    # print("\nfile_path_variable = ", tempdir)
    return tempdir

def SeperateFolders(address):
    os.chdir(address)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    methodSmells=['comments.csv', 'feature-envy.csv', 'brain-method.csv', 'long-parameter-list.csv', 'message-chains.csv']
    for smell in all_filenames:
        source=address+'/'+smell
        print('source : ',source)
        if smell in methodSmells:
            destination=address+'/method'
            print('methoddest : ', destination)
        else:
            destination=address+'/class'
            print('classdest : ', destination)
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(source, destination)


def main(address):
    # address=browsefile_path()
    my_list = os.listdir(address)
    for folder in my_list:
        path=address+'/'+folder
        print(path)
        SeperateFolders(path)

# main()