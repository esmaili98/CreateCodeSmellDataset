import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import tkinter as tk
import os
from tkinter import filedialog

def browsefile_path(title="Select the file"):
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title=title)
    return files[0]

def read_dataset():
    address=browsefile_path(title="Select \".csv\" dataset file")
    df = pd.read_csv(address)
    return df

def PrepareTrainTestData():
    wine=read_dataset()
    features = wine.iloc[:, 1:-1].to_numpy()
    label = wine.iloc[:, -1].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=42)

    # sc = StandardScaler()
    # x_train = sc.fit_transform(x_train)
    # x_test = sc.fit_transform(x_test)
    return [features, label, x_train, x_test, y_train, y_test]

def GradientBoosting():
    data = PrepareTrainTestData()
    x_train = data[2]
    x_test = data[3]
    y_train = data[4]
    y_test = data[5]

    gbm = GradientBoostingClassifier(n_estimators=5000,
                                           learning_rate=0.05,
                                           max_depth=60,
                                           subsample=0.5,
                                           validation_fraction=0.2,
                                           n_iter_no_change=20,
                                           max_features='auto',
                                           verbose=1)
    gbm.fit(x_train, y_train)
    pred_rfc = gbm.predict(x_test)

    print(str(classification_report(y_test, pred_rfc)))
    print('\n\n' + str(confusion_matrix(y_test, pred_rfc)))
    print('\n\n' + str(accuracy_score(y_test, pred_rfc)))

GradientBoosting()