import glob
import pandas as pd
import tkinter
from tkinter import filedialog
import os
# import AggregateSmellCSVFiles
import shutil


def browsefile_path():
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)

    print("\nfile_path_variable = ", tempdir)
    return tempdir

def AggregateCSVFiles(address):
    dirList=os.listdir(address)
    smellNames = ['Class_Data_Should_Be_Private', 'Complex_Class', 'Inappropriate_Intimacy', 'Large_Class',
                  'Lazy_Class', 'Middle_Man', 'Refused_Bequest', 'Spaghetti_Code', 'Speculative_Generality', 'Comments',
                  'Feature_Envy', 'Long_Methods', 'Long_Parameter_List', 'Message_Chains','Blob']
    for dir in dirList:
        dirList2=os.listdir(address+'/'+dir)
        for dir2 in dirList2:
            address2=address+'/'+dir
            os.chdir(address2+'/'+dir2)
            extension = 'csv'
            all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
            print(all_filenames)
            for smellcsvfile in all_filenames:
                for smellname in smellNames:
                    if smellname in smellcsvfile:
                        source=address2+'/'+dir2+'/'+smellcsvfile
                        destination=address+'/Aggregated/'+smellname
                        if not os.path.exists(destination):
                            os.makedirs(destination)
                        print('source: ',source)
                        print('dest: ',destination)
                        shutil.move(source, destination)


def combine(address,saveAddress,directory):
    # address=browsefile_path()
    os.chdir(address)
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    #combine all files in the list
    concatInputList=list()
    for filename in all_filenames:
        try:
            concatInputList.append(pd.read_csv(filename))
        except:
            continue
    if concatInputList!=[]:
        combined_csv = pd.concat(concatInputList)
        # print('type: ',type(combined_csv))
    else:
       combined_csv = pd.DataFrame()
    print(combined_csv)
    #export to csv


    dirpath = saveAddress
    # foldername = os.path.basename(dirpath)
    if not os.path.exists(saveAddress):
        os.makedirs(saveAddress)
    savedirectory=saveAddress+'/'+directory+"_CombinedAll"+'/'
    if not os.path.exists(savedirectory):
        os.makedirs(savedirectory)
    name=all_filenames[0][0:-4]+"_CombinedAll.csv"
    combined_csv.to_csv( savedirectory+ name, index=False, encoding='utf-8-sig')

def readDirectories(address):
    # address = browsefile_path()


    index = len(address) - 1
    lastslash = 0
    # print('Address : ',smellCSVFileAddress)
    while (index > 0):
        if address[index] == '/':
            lastslash = index
            index2 = index - 1
            while (index2 > 0):
                if address[index2] == '/':
                    secondlastslash = index2
                    break
                else:
                    index2 -= 1
            break
        else:
            index -= 1


    folders_list = os.listdir(address)
    for directory in folders_list:
        final_address=address+'/'+directory
        combine(final_address,address+'/'+address[secondlastslash:lastslash]+'_Combined',directory)

def main():
    address = browsefile_path()
    AggregateCSVFiles(address)
    readDirectories(address+'/Aggregated')

while(True):
    main()