from sklearn.neighbors import LocalOutlierFactor
import pandas as pd
import tkinter as tk
from tkinter import filedialog


def LOF(address):
    df = pd.read_csv(address)
    x = df.iloc[:, 1:-1] # to remove entities name and label
    print(x.head())
    # x=wine.values()
    benchmark = pd.read_csv(address)
    labels = list(benchmark.iloc[:, -1])

    clf = LocalOutlierFactor(n_neighbors=int((len(labels))/5))
    lofResult =list(clf.fit_predict(x))
#################################################
    index = len(address) - 1
    while address[index] != '/':
        index -= 1

    path = address[:index] + '\\' + 'LOFresult.txt'
    # if  os.path.exists(path):
    #     os.remove(path)
    logfile = open(path, 'a')

######################################################

    print('Number of anomalies: {}'.format( lofResult.count(-1)))

    logfile.writelines('\n\nNumber of anomalies: {}'.format( str(lofResult.count(-1))))






    print('Number of smells: {}'.format(labels.count(1)))
    # print(ifResult.head())
    logfile.writelines('\nNumber of smells: {}'.format(str(labels.count(1))))

    print('len of anomaly lables column: {}'.format(str(len(lofResult))))
    print('len of smell labels column: {}'.format(str(len(labels))))

    logfile.writelines('\nlen of anomaly lables column: {}'.format(str(len(lofResult))))
    logfile.writelines('\nlen of smell labels column: {}'.format(str(len(labels))))

    tp=0;tn=0;fp=0;fn=0

    for item in range(len(lofResult)):
        if lofResult[item]==-1 and labels[item]==1:
            tp+=1
        elif lofResult[item]==1 and labels[item]==0:
            tn+=1
        elif lofResult[item]==-1 and labels[item]==0:
                fp+=1
        elif lofResult[item]==1 and labels[item]==1:
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

    logfile.writelines('\nNeighbors: {}'.format(str(clf.n_neighbors)))
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
LOF(address)
