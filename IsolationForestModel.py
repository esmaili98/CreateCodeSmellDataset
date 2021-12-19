import pandas as pd

from sklearn.ensemble import IsolationForest
import tkinter as tk
from tkinter import filedialog

def IsolationForrest(address):
    df = pd.read_csv(address)
    x = df.iloc[:, 1:-1] # to remove entities name and label
    print(x.head())
    # x=wine.values()

    clf = IsolationForest(contamination=.04)
    clf.fit(x)
    ifResult =list(clf.predict(x))
#################################################
    index = len(address) - 1
    while address[index] != '/':
        index -= 1

    path = address[:index] + '\\' + 'IFresult.txt'
    # if  os.path.exists(path):
    #     os.remove(path)
    logfile = open(path, 'a')

######################################################

    print('Number of anomalies: {}'.format( ifResult.count(-1)))

    logfile.writelines('\n\nNumber of anomalies: {}'.format( str(ifResult.count(-1))))



    benchmark=pd.read_csv(address)
    labels = list(benchmark.iloc[:, -1])

    print('Number of smells: {}'.format(labels.count(1)))
    # print(ifResult.head())
    logfile.writelines('\nNumber of smells: {}'.format(str(labels.count(1))))

    print('len of anomaly lables column: {}'.format(str(len(ifResult))))
    print('len of smell labels column: {}'.format(str(len(labels))))

    logfile.writelines('\nlen of anomaly lables column: {}'.format(str(len(ifResult))))
    logfile.writelines('\nlen of smell labels column: {}'.format(str(len(labels))))

    tp=0;tn=0;fp=0;fn=0

    for item in range(len(ifResult)):
        if ifResult[item]==-1 and labels[item]==1:
            tp+=1
        elif ifResult[item]==1 and labels[item]==0:
            tn+=1
        elif ifResult[item]==-1 and labels[item]==0:
                fp+=1
        elif ifResult[item]==1 and labels[item]==1:
                fn+=1
    precision=tp/(tp+fp)
    recall=tp/(tp+fn)

    fmeasure=(2*recall*precision)/(precision+recall)

    accuracy=(tp+tn)/(tp+tn+fn+fp)

    print('TP: {}, FP: {}, TN: {}, FN: {}'.format(tp,fp,tn,fn))
    print('Precision: {}'.format(precision))
    print('Recal: {}'.format(recall))
    print('f-measure: {}'.format(fmeasure))
    print('accuracy: {}'.format(accuracy))

    logfile.writelines('\nContamination: {}'.format(str(clf.contamination)))
    logfile.writelines('\nTP: {}, FP: {}, TN: {}, FN: {}'.format(str(tp),str(fp),str(tn),str(fn)))
    logfile.writelines('\nPrecision: {}'.format(str(precision)))
    logfile.writelines('\nRecall: {}'.format(str(recall)))
    logfile.writelines('\nf-measure: {}'.format(str(fmeasure)))
    logfile.writelines('\naccuracy: {}'.format(str(accuracy)))


def browsefile_path():
    root = tk.Tk()
    root.withdraw()

    files = filedialog.askopenfilenames()
    return files[0]

address=browsefile_path()
print(address)
IsolationForrest(address)
