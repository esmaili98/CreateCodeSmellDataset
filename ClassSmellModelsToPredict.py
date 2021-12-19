import csv
import os
import statistics

import joblib
import pandas as pd
from tkinter import filedialog
import tkinter as tk
import GiveUNDdatabase
import Main_metrics
import RemoveDuplicatesANDnonValues
from shutil import copy


class clsComputeMetricsForInputProject:
    def createUNDdb(self):
        obj=GiveUNDdatabase.GvieUNDdatabase()
        db=obj.give_db()
        return db

    def computeMetrics(self):
        db=self.createUNDdb()
        obj=Main_metrics.cls_arangement()
        classMetrics=obj.returnClassMetrics(db)
        udbadd=str(db)
        return [classMetrics,udbadd]

    def saveCSVFile(self):
        computemetrics_ouptput=self.computeMetrics()
        classMetrics=computemetrics_ouptput[0]
        udbadd=computemetrics_ouptput[1]


        index = len(udbadd) - 1
        while udbadd[index] != '\\':
            index -= 1
        udbName = udbadd[index + 1:][:-4]
        # print(classMetrics)
        classMetrics[1].insert(0, 'longname')
        for i in range(len(classMetrics[0])):
            classMetrics[2][i].insert(0, classMetrics[0][i])

        for i in range(len(classMetrics[2])):
            classMetrics.append(classMetrics[2].pop(0))
        # print(classMetrics)
        classMetrics.pop(0)
        classMetrics.pop(1)
        # print(classMetrics)
        desktopadd = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        address= desktopadd+'/Prediction/'+ udbName +'/ClassSmells/' + udbName + 'ClassMetrics.csv'
        if  not os.path.exists(desktopadd +'/Prediction/'+ udbName +'/ClassSmells/'):
            os.makedirs(desktopadd+'/Prediction/'+ udbName +'/ClassSmells/')

        with open(address,'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(classMetrics)

        ###################################
        # copy udb file to prediction folder for refactor opprtunity
        copy(udbadd, desktopadd + '/Prediction/' + udbName)
        ###################################

        return address
    def main(self):
        address=self.saveCSVFile()
        return address
class clsCleanProjectMetrics:
    # address='C:/Users/Sadaf/Desktop/Prediction/classMetrics/' + 'projectName' + '.csv'

    def removeDuplicates(self,address):
        RemoveDuplicatesANDnonValues.cleandup(address)

    def removeNone(self,address):
        RemoveDuplicatesANDnonValues.cleanNoneItems(address[:-4]+'_CleanedDup.csv')

    def cleanNone(self,address):
        address=address[:-4]+'_Cleaned.csv'
        df = pd.read_csv(address)
        cols=df.columns
        for col in range(1,len(cols)-1):
            newValue = self.calColumnMedian(df, cols[col])
            df[cols[col]].replace({float('nan'):newValue},inplace=True)
        df.to_csv(address[:-4]+'ByMedian.csv',index=False, encoding='utf-8')
        # os.remove(address)
        return address[:-4]+'ByMedian.csv'

    def calColumnMedian(self,df,col):
        values = list(df[col])
        values = [x for x in values if str(x) != 'nan']
        return statistics.median(values)
    def main(self,address):
        self.removeDuplicates(address)
        self.removeNone(address)
        addresscleaned=self.cleanNone(address)
        return addresscleaned


class clsprediction:
    def browsefile_path(self,title="Select the file"):
        root = tk.Tk()
        root.withdraw()
        files = filedialog.askopenfilenames(title=title)
        return files[0]

    def loadModelToPredict(self,addresscleaned):
        # address=self.browsefile_path()
        df = pd.read_csv(addresscleaned)
        features = df.iloc[:, 1:].to_numpy()
        entities=df.iloc[:, 0]
        print(features)

        Modeladdress=self.browsefile_path(title="Select \".sav\" model file")
        loaded_model=joblib.load(Modeladdress)


        result=loaded_model.predict(features)
        # print(result)
        smells=list()
        for i in range(len(result)):
            if result[i]==1:
                smells.append(entities[i])
        print(smells)


        ind = len(Modeladdress) - 1
        while Modeladdress[ind] != '/':
            ind -= 1
        smellName=Modeladdress[ind+1:-4]

        _index=smellName.index('_')
        smellName=smellName[:_index]

        index = len(addresscleaned) - 1
        while addresscleaned[index] != '/':
            index -= 1
        path = addresscleaned[:index] + '/Smells/' + smellName +'.txt'
        # print(path)
        if  not os.path.exists(addresscleaned[:index] + '/Smells'):
            os.makedirs(addresscleaned[:index] + '/Smells')

        logfile = open(path, 'w')
        for smell in smells:
            logfile.writelines('{}\n'.format(str(smell)))

    def main(self,addresscleaned):
        self.loadModelToPredict(addresscleaned)

if __name__ == '__main__':
    address=clsComputeMetricsForInputProject().main()
    addresscleaned=clsCleanProjectMetrics().main(address)
    while True:
        clsprediction().main(addresscleaned)