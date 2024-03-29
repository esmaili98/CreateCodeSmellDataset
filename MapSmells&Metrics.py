import tkinter
from tkinter import filedialog
import os
import csv
import UndMetrics

def undmetricsget():
    return UndMetrics.createCSVfiles()

def MatchLongNames(smellcsvfile):
    correctedname=list()
    for enityname in smellcsvfile:
        # print("entity name: ",enityname)
        # print("entity last: ", enityname[-1])
        smeicoutn=enityname.count(';')
        firstsemiindex = enityname.index(';')
        if smeicoutn==1:
            if enityname[firstsemiindex-5:firstsemiindex]=='.java':
                metricname= str(enityname[firstsemiindex+2:]) + '.' + enityname[:firstsemiindex-5]
            else:
                metricname = str(enityname[firstsemiindex + 2:]) + '.' + enityname[:firstsemiindex]


        elif smeicoutn==2:
            secondsemiindex = enityname.index(';', firstsemiindex + 1)
            if enityname[-1]==';' or enityname[-2]==';':
                if enityname[firstsemiindex - 5:firstsemiindex] == '.java':
                    metricname= str(enityname[firstsemiindex+2:-1]) + '.' + enityname[:firstsemiindex-5]
                else:
                    metricname = str(enityname[firstsemiindex + 2:-1]) + '.' + enityname[:firstsemiindex]
            else:
                try:
                    i=int(enityname[secondsemiindex+1:])
                    if enityname[firstsemiindex - 5:firstsemiindex] == '.java':
                        metricname = str(enityname[firstsemiindex + 2:-1]) + '.' + enityname[:firstsemiindex - 5]
                    else:
                        metricname = str(enityname[firstsemiindex + 2:-1]) + '.' + enityname[:firstsemiindex]
                except:
                    if enityname[secondsemiindex - 5:secondsemiindex] == '.java':
                        metricname = str(enityname[secondsemiindex + 2:]) + '.' + enityname[firstsemiindex+2:secondsemiindex - 5]+ '.' + enityname[:firstsemiindex]
                    else:
                        metricname = str(enityname[secondsemiindex + 2:]) + '.' + enityname[firstsemiindex+2:secondsemiindex]+ '.' + enityname[:firstsemiindex]


        elif smeicoutn==3:
            secondsemiindex = enityname.index(';', firstsemiindex+1)
            thirdsemiindex = enityname.index(';', secondsemiindex + 1)
            if enityname[-1]==';':
                if enityname[firstsemiindex - 5:firstsemiindex] == '.java':
                    metricname = str(enityname[firstsemiindex + 2:secondsemiindex]) + '.' + enityname[:firstsemiindex - 5]
                else:
                    metricname = str(enityname[firstsemiindex + 2:secondsemiindex]) + '.' + enityname[:firstsemiindex]
            else:
                if enityname[secondsemiindex - 5:secondsemiindex] == '.java':
                    metricname = str(enityname[secondsemiindex + 2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex - 5] + '.' + enityname[:firstsemiindex]
                else:
                    metricname = str(enityname[secondsemiindex + 2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex] + '.' + enityname[:firstsemiindex]


        elif smeicoutn==4:
            secondsemiindex = enityname.index(';', firstsemiindex + 1)
            thirdsemiindex = enityname.index(';', secondsemiindex + 1)
            if enityname[-1] == ';' or enityname[-2] == ';':
                if enityname[firstsemiindex - 5:firstsemiindex] == '.java':
                    metricname= str(enityname[firstsemiindex+2:secondsemiindex]) + '.' + enityname[:firstsemiindex-5]
                else:
                    metricname = str(enityname[firstsemiindex + 2:secondsemiindex]) + '.' + enityname[:firstsemiindex]
            else:
                if enityname[secondsemiindex - 5:secondsemiindex] == '.java':
                    metricname= str(enityname[secondsemiindex+2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex-5]+ '.' + enityname[:firstsemiindex]
                else:
                    metricname= str(enityname[secondsemiindex+2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex]+ '.' + enityname[:firstsemiindex]

        elif smeicoutn==5:
            secondsemiindex = enityname.index(';', firstsemiindex + 1)
            thirdsemiindex = enityname.index(';', secondsemiindex + 1)
            if enityname[secondsemiindex - 5:secondsemiindex] == '.java':
                metricname = str(enityname[secondsemiindex + 2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex - 5] + '.' + enityname[:firstsemiindex]
            else:
                metricname = str(enityname[secondsemiindex + 2:thirdsemiindex]) + '.' + enityname[firstsemiindex+2:secondsemiindex] + '.' + enityname[:firstsemiindex]


        elif smeicoutn==7:
            secondsemiindex = enityname.index(';', firstsemiindex + 1)
            if enityname[firstsemiindex - 5:firstsemiindex] == '.java':
                metricname = str(enityname[firstsemiindex + 2:secondsemiindex]) + '.' + enityname[:firstsemiindex - 5]
            else:
                metricname = str(enityname[firstsemiindex + 2:secondsemiindex]) + '.' + enityname[firstsemiindex]
        else:
            print('number of semi : ',smeicoutn)
        correctedname.append(metricname)

    return correctedname

def browsefile_path():
    root = tkinter.Tk()
    root.withdraw()  # use to hide tkinter window
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print("You chose: %s" % tempdir)

    print("\nfile_path_variable = ", tempdir)
    return tempdir


def readallsmellcsvfiles():
    path = browsefile_path()
    os.chdir(path)
    allsmellcsvrows=list()
    allfilenames=list()
    for file in os.listdir():
        if file.endswith(".csv"):
            file_path = f"{path}\{file}"
            index1 = path.index('/', len(path) - 45)
            index2 = path.index('/', len(path) - 19)
            name = file[0:-4] + '_' + path[index1 + 1:index2]+".csv"
            allfilenames.append(name)
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                listcsvsmellrows = list()
                for row in reader:
                    listcsvsmellrows.append(row[0])
                allsmellcsvrows.append(listcsvsmellrows)
    # print(allsmellcsvrows)
    return [allfilenames,allsmellcsvrows]

# def readcsvsmellfile(address):
#     with open(address, 'r') as file:
#         reader = csv.reader(file)
#         listcsvsmellfile=list()
#         for row in reader:
#             listcsvsmellfile.append(row[0])
#         return listcsvsmellfile

def csvsmellfilecorrection(csvsmellfiles):
    csvsmellfilecorrected=list()
    for csvsmellfile in csvsmellfiles:
        csvsmellfilecorrected.append(MatchLongNames(csvsmellfile))
    return csvsmellfilecorrected

def CreateCSVSmellMetricFile():
    # address='C://Users//Sadaf//PycharmProjects//Compute_Metrics//ArgoUML-0.10.1-src_OK//Validated//candidate_Complex_Class.csv'
    defaultPath = os.getcwd()
    print('select source file to compute metrics:')
    undmetricslist=undmetricsget()
    # print('111111',undmetricslist[0][1])
    # print('111111', undmetricslist[0][2])

    # first class level then method level
    for level in range(2):
        removecandidates = list()
        print('select csv smell files:')
        csvsmellfiles = readallsmellcsvfiles()
        csvsmellfilecorrected = csvsmellfilecorrection(csvsmellfiles[1])
        csvsmellfilesname = csvsmellfiles[0]
        # each smell csv file
        for smellfile in range(len(csvsmellfilecorrected)):
            missCount=0
            extracount=0
            hitCount=0

            finalcsvfile=list()
            finalcsvfile.append(undmetricslist[level][0])

            # each entity in smell csv file
            for entity in csvsmellfilecorrected[smellfile]:
                flag = -1
                print('entity',entity)
                i=0
                limit=len(undmetricslist[level])

                # each entity in metrics file
                while i < limit:
                    if undmetricslist[level][i]!=[] and undmetricslist[level][i][0]==entity:
                        if flag==-1:
                            flag=1
                            hitCount += 1
                        elif flag==0:
                            extracount+=1
                        print('entered')
                        finalcsvfile.append(undmetricslist[level][i])
                        # print('11111111',undmetricslist[level][i])
                        removecandidates.append(undmetricslist[level][i])
                        flag=0
                    i += 1

                if flag==-1:
                    missCount+=1

            # print(finalcsvfile)

            if len(finalcsvfile)==1:
                finalcsvfile.pop()

            if missCount!=0:
                address = defaultPath +'\\result\\' + csvsmellfilesname[smellfile][0:-4]+'_MissedEntity.csv'
            elif extracount!=0:
                address = defaultPath +'\\result\\Extras\\' + csvsmellfilesname[smellfile][0:-4] + '_ExtraEntity.csv'
            else:
                address=defaultPath+ '\\result\\'+csvsmellfilesname[smellfile]
            with open(address, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(finalcsvfile)
            print('______________________'+csvsmellfilesname[smellfile]+'Smell Metrics CSV file has been created______________________')
            print('____________number of hits : ',hitCount,' number of extras : ',extracount,' number of missed : ',missCount ,'____________')

        print('______Number of smelly elements are : ',len(removecandidates),'______')
        # print(removecandidates)
        for removeelement in  removecandidates:
            try:
                undmetricslist[level].remove(removeelement)
            except:
                continue
        # print('@@@@@',undmetricslist[0])
        if level==0:
            address =defaultPath + '\\result\\class_nonsmell.csv'
        else:
            address = defaultPath + '\\result\\method_nonsmell.csv'
        with open(address, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(undmetricslist[level])



CreateCSVSmellMetricFile()