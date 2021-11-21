import os
import statistics
import tkinter as tk
from collections import Counter
from tkinter import filedialog
import glob

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import queue
from threading import Thread



class CreateModel:


    def PrepareTrainTestData(self,wine):
        features = wine.iloc[:, 1:-1].to_numpy()
        label = wine.iloc[:, -1].to_numpy()

        x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=0)

        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.fit_transform(x_test)
        return [features,label,x_train,x_test,y_train,y_test]

    def RandomForest(self,df,address):
        data=self.PrepareTrainTestData(df)
        x_train=data[2]
        x_test=data[3]
        y_train=data[4]
        y_test=data[5]

        rfc = RandomForestClassifier(n_estimators=200,random_state=0)
        rfc.fit(x_train, y_train)
        pred_rfc = rfc.predict(x_test)

        index = len(address) - 1
        while address[index] != '/':
            index -= 1

        path = address[:index] + '/' + 'RFresult.txt'

        logfile = open(path, 'a')
        logfile.writelines(str(classification_report(y_test, pred_rfc)))
        logfile.writelines('\n\n'+str(confusion_matrix(y_test, pred_rfc)))
        logfile.writelines('\n\n'+str(accuracy_score(y_test, pred_rfc)))


    def get_score(self,arg):
        model=arg[0]
        X_train=arg[1]
        X_test=arg[2]
        y_train=arg[3]
        y_test=arg[4]
        model.fit(X_train, y_train)
        pred_rfc=model.predict(X_test)
        measures=classification_report(y_test, pred_rfc)
        # print(measures)
        p0=(float(measures[74:78]))
        r0=(float(measures[84:88]))
        f0=(float(measures[94:98]))
        p1=(float(measures[128:132]))
        r1=(float(measures[138:142]))
        f1=(float(measures[148:152]))




        return [p0,r0,f0,p1,r1,f1,model.score(X_test, y_test),model]

    def fold_cross_validation(self,features,label,address):
        scores_rf = []
        folds = StratifiedKFold(n_splits=10)
        index = len(address) - 1
        while address[index] != '/':
            index -= 1
        f1 = 0
        number=0

        ques = list()
        for i in range(10):
            ques.append(queue.Queue())

        classthreads = list()

        for train_index, test_index in folds.split(features, label):

            x_train, x_test, y_train, y_test = features[train_index], features[test_index], \
                                               label[train_index], label[test_index]
            classthreads.append(Thread(target=lambda q, arg1: q.put(self.get_score(arg1)), args=(ques[number], \
                                                                [RandomForestClassifier(n_estimators=200, random_state=0), x_train, x_test, y_train, y_test])))
            number+=1

        for thread in classthreads:
                thread.start()
        for thread2 in classthreads:
                thread2.join()
        for p in range(10):
            getscoreoutput=(ques[p].get())

            print(getscoreoutput)
            scores_rf.append(getscoreoutput)
            # scores_logistic.append(get_score(LogisticRegression(solver='liblinear', multi_class='ovr'), X_train, X_test, y_train, y_test))
            # scores_svm.append(get_score(SVC(gamma='auto'), X_train, X_test, y_train, y_test))

            if f1<getscoreoutput[5]:
                f1=getscoreoutput[5]
                model=getscoreoutput[7]
                #delete last sav file
                test = os.listdir(address[:index])

                for item in test:
                    if item.endswith(".sav"):
                        os.remove(os.path.join(address[:index], item))
                 #save new sav file
                filename = address[:index]+'\\'+str(getscoreoutput[3])+'_'+str(getscoreoutput[4])+'_'+str(getscoreoutput[5])+'__'+str(p)+'th_model.sav'
                joblib.dump(model, filename)


        print('Random Forest 10 fold cross validation Scores: ')
        print(scores_rf)
        print('Random Forest zero Precision mean : {}'.format(statistics.mean([i[0] for i in scores_rf])))
        print('Random Forest zero recall mean : {}'.format(statistics.mean([i[1] for i in scores_rf])))
        print('Random Forest zero fscore mean : {}'.format(statistics.mean([i[2] for i in scores_rf])))
        print('Random Forest one Precision mean : {}'.format(statistics.mean([i[3] for i in scores_rf])))
        print('Random Forest one recall mean : {}'.format(statistics.mean([i[4] for i in scores_rf])))
        print('Random Forest one fscore mean : {}'.format(statistics.mean([i[5] for i in scores_rf])))

        print('Random Forest mean scores: {}'.format(statistics.mean([i[6] for i in scores_rf])))



        path = address[:index] + '\\' + 'RFresult.txt'
        logfile = open(path, 'a')
        logfile.writelines('\n\nRandom Forest 10 fold cross validation Scores: ')
        logfile.writelines(str(scores_rf))
        logfile.writelines('\nRandom Forest zero precision mean: {}'.format(str(statistics.mean([i[0] for i in scores_rf]))))
        logfile.writelines('\nRandom Forest zero recall mean: {}'.format(str(statistics.mean([i[1] for i in scores_rf]))))
        logfile.writelines('\nRandom Forest zero fscore mean: {}'.format(str(statistics.mean([i[2] for i in scores_rf]))))
        logfile.writelines('\nRandom Forest one precision mean: {}'.format(str(statistics.mean([i[3] for i in scores_rf]))))
        logfile.writelines('\nRandom Forest one recall mean: {}'.format(str(statistics.mean([i[4] for i in scores_rf]))))
        logfile.writelines('\nRandom Forest one fscore mean: {}'.format(str(statistics.mean([i[5] for i in scores_rf]))))

        logfile.writelines('\nRandom Forest mean scores: {}'.format(str(statistics.mean([i[6] for i in scores_rf]))))

    def main(self,df,address):
        data=self.PrepareTrainTestData(df)
        features=data[0]; label=data[1]

        self.RandomForest(df, address)

        self.fold_cross_validation(features,label,address)




class PrepareData:
    def browsefile_path(self):
        root = tk.Tk()
        root.withdraw()

        files = filedialog.askopenfilenames()
        return files[0]

    def addLabel(self,address):

        df = pd.read_csv(address)
        label = 1
        labels = [label for i in range(len(df))]
        df['label'] = labels
        print(df.head())
        df.to_csv(address[:-4] + '_Labeled.csv', index=False, encoding='utf-8')
        os.remove(address)

        return address[:-4] + '_Labeled.csv'


    def shuffle(self,address):

        df = pd.read_csv(address)
        ds = df.sample(frac=1)
        ds.to_csv(address[:-4] + '_Shuffled.csv', index=False, encoding='utf-8')
        os.remove(address)
        return address[:-4] + '_Shuffled.csv'

    def combine(self,address,name):
        os.chdir(address)
        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        # combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
        # export to csv

        combined_csv.to_csv(address+'/'+name+'NOSmell.csv', index=False, encoding='utf-8-sig')

        return address+'/'+name+'NOSmell.csv'



    def calColumnMean(self,df,col):
        values=list(df[col])
        # print(values)
        values=[x for x in values if str(x) != 'nan']
        # print(values)
        return statistics.mean(values)

    def calColumnMedian(self,df,col):
        values = list(df[col])
        # print(values)
        values = [x for x in values if str(x) != 'nan']
        # print(values)
        return statistics.median(values)

    def calColumnMostCommonMean(self, df, col):
        values = list(df[col])
        # print(values)
        values = [x for x in values if str(x) != 'nan']
        # print(values)

        iterations = Counter(values)

        top_10_items=iterations.most_common(11)

        most_common_list=[ x[0] for x in top_10_items]
        if 0 in most_common_list:
            most_common_list.remove(0)
        return statistics.mean(most_common_list)


    def replace_with_new_value(self,address):
        df = pd.read_csv(address)
        try:
            df.drop('WOC', inplace=True, axis=1)
        except:
            pass

        cols=df.columns
        for col in range(1,len(cols)-1):
            # newValue=self.calColumnMean(self,df,cols[col])
            newValue = self.calColumnMedian(df, cols[col])
            # newValue = self.calColumnMostCommonMean(self, df, cols[col])

            df[cols[col]].replace({float('nan'):newValue},inplace=True)
        df.to_csv(address[:-4]+'ByMedian.csv',index=False, encoding='utf-8')
        os.remove(address)
        return address[:-4]+'ByMedian.csv'

    def main(self):
        address=self.browsefile_path()
        # label=input('Enter label (0,1): ')
        addressLabeled=self.addLabel(address)

        addressCleaned=self.replace_with_new_value(addressLabeled)
        index=len(addressCleaned)-1
        while addressCleaned[index]!='/':
            index-=1
        combineAddress=addressCleaned[:index]
        combined_address=self.combine(combineAddress,addressCleaned[index+1:-4])
        address_shuffeld=self.shuffle(combined_address)

        print(address_shuffeld)
 
        dfshuffeld = pd.read_csv(address_shuffeld)
        obj=CreateModel()
        obj.main(dfshuffeld,address_shuffeld)

obj_prepare=PrepareData()
obj_prepare.main()