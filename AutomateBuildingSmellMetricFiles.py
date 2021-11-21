import shutil
import tkinter
from tkinter import filedialog
import os
import MapSmellsANDMetrics
import SeperateClassMethodSmellsFolders

def browsefile_path():
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)

    print("\nfile_path_variable = ", tempdir)
    return tempdir

def autoBuild(dirAddress):
    # a=input()
    # print(a)
    # dirAddress=browsefile_path()
    smelldiraddress=dirAddress+'/smell'
    metricdiraddress = dirAddress + '/metric'
    smelldir_list = os.listdir(smelldiraddress)
    metricdir_list=os.listdir(metricdiraddress)
    print('smell', smelldir_list)
    print('metric', metricdir_list)
    # dir_list=sorted(dir_list)
    # print('sorted_test',dir_list)
    resultdir_list = os.listdir('C:\\Users\\Sadaf\\PycharmProjects\\CreateDataset\\result')
    if resultdir_list!=[]:
        lastresultdir = resultdir_list[-1]
        startdir=smelldir_list.index(lastresultdir)+1
    else:
        startdir=0
    for dir in range(startdir,len(smelldir_list)):
        print('dir',dir)
        metricdir=metricdiraddress+'/'+metricdir_list[dir]
        print('sourceadd', metricdir)
        # index=int((len(dir_list)/2))+dir
        classSmellDir=smelldiraddress+'/'+smelldir_list[dir]+'/class'
        print('classsmelladd', classSmellDir)
        methodSmellDir = smelldiraddress + '/' + smelldir_list[dir] + '/method'
        print('methodsmelladd', methodSmellDir)

        MapSmellsANDMetrics.CreateCSVSmellMetricFile(metricdir,classSmellDir,methodSmellDir)


def main():
    address=browsefile_path()
    SeperateClassMethodSmellsFolders.main(address+'/smell')
    autoBuild(address)


main()