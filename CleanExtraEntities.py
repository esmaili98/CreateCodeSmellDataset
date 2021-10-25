import csv
import tkinter as tk
from tkinter import filedialog


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

def sort(input,secondIndex):
    if secondIndex==1 or secondIndex==-1:
        s=sorted(sorted(input[1:], key=lambda x: float(x[secondIndex]),reverse=False), key=lambda x: x[0], reverse=False)
    else:
        s=sorted(input[1:],key=lambda x:x[0],reverse=False)
    # print('s: ',s)
    return s

def cleanNoneElements(smellCSVList):
    removecadidates=list()
    for entity in smellCSVList:
        if entity[-1]=='':
            removecadidates.append(entity)
    for candidate in removecadidates:
        smellCSVList.remove(candidate)
    return smellCSVList

def cleanCnadidateCSVFile():
    smellCSVFileAddress=browsefile_path()
    smellCSVList = readcsvsmellfile(smellCSVFileAddress)
    if 'Long_Methods' in smellCSVFileAddress or 'Large_Class' in smellCSVFileAddress:
        sortedFile=sort(smellCSVList,1)
    elif 'Long_Parameter_List' in smellCSVFileAddress:
        cleanedsmellCSVList=cleanNoneElements(smellCSVList)
        sortedFile=sort(cleanedsmellCSVList,-1)
    else:
        sortedFile = sort(smellCSVList, 0)


    #determine remove candidates
    removeCandidates=list()
    if 'Long_Methods' in smellCSVFileAddress or 'Long_Parameter_List' in smellCSVFileAddress or 'Large_Class' in smellCSVFileAddress:
        for entity in range(1,len(sortedFile)):
            if sortedFile[entity][0]==sortedFile[entity-1][0]:
                removeCandidates.append(sortedFile[entity-1])
            else:
                pass
    else:
        groupbylist=[[sortedFile[0],1]]
        entity=1
        while entity < len(sortedFile):
            # if sortedFile[entity]!=sortedFile[entity-1]:              privious code
            if sortedFile[entity][0] != sortedFile[entity - 1][0]:
                groupbylist.append([sortedFile[entity],1])
                entity+=1
            else:
                groupbylist[-1][1]=groupbylist[-1][1]+1
                entity+=1
        # tempcandidates=list()
        print(groupbylist)
        UncompeleteRemoveCandidates=list()
        for i in groupbylist:
            if i[1]>1:
                UncompeleteRemoveCandidates.append(i[0][0])
        for entity in sortedFile:
            if entity[0] in UncompeleteRemoveCandidates:
                removeCandidates.append(entity)

        # for i in tempcandidates:
        #     for j in sortedFile:
        #         if j[0]==i:
        #             removeCandidates.append(j)

    # determine save address
    index = len(smellCSVFileAddress)-1
    while (True):  # to find the last '/' to create address
        if smellCSVFileAddress[index] == '/':
            break
        else:
            index-=1
    logaddress = smellCSVFileAddress[0:index]

    logfile = open(logaddress+'/'+smellCSVFileAddress[index+1:-4]+'clean_Log.txt', 'a')
    #remove candidates
    for candidate in removeCandidates:
        print('candidate: ',candidate)
        smellCSVList.remove(candidate)
        print('list: ',smellCSVList)
        # write logs
        logfile.writelines(str(candidate)+'\n')



    with open(smellCSVFileAddress[0:-4]+'--'+str(len(removeCandidates))+'_Cleaned.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(smellCSVList)


    index=len(smellCSVFileAddress)-1
    lastslash=0
    # print('Address : ',smellCSVFileAddress)
    while(index>0):
        if smellCSVFileAddress[index]=='/':
            lastslash=index
            index2=index-1
            while(index2>0):
                if smellCSVFileAddress[index2] == '/':
                    secondlastslash=index2
                    break
                else:
                    index2-=1
            break
        else:
            index-=1
    with open(smellCSVFileAddress[0:secondlastslash]+smellCSVFileAddress[lastslash:-4]+'--'+str(len(removeCandidates))+'_Cleaned.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(smellCSVList)


while(True):
    cleanCnadidateCSVFile()