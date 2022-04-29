'''
@author: Massaro, Trotti & Marino
'''

from model_performance import accuracy, MAE, kfold
import pandas as pd
from warnings import simplefilter
from sklearn.model_selection import train_test_split
from sklearn.tree._classes import DecisionTreeClassifier
from questions import interaction
from prolog import ospedalization

if __name__ == '__main__':
    simplefilter(action='ignore', category=FutureWarning)
    
    data = pd.read_csv(r".\..\dataset\datasetUltimate.csv")
    
    y = data.Disorder
    x = data.drop('Disorder', axis=1)

    y=y.astype('int')
    x=x.astype('int')
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33)
    
    model = DecisionTreeClassifier()
    
    model.fit(x_train, y_train)    
    p_train = model.predict(x_train)
    p_test = model.predict(x_test)

    accuracy(y_train, y_test, p_train, p_test)
    MAE(y_train, y_test, p_train, p_test)
    kfold(model, x, y)
    
    us = interaction()
    ris = us.getValues()
    #ospedalization(ris)
    
    for index, row in ris.iterrows():
        if(row[0] == 'Yes'):
            row[0]=1
        else:
            row[0]=0
    ris = ris.T
    
    p = model.predict(ris)
    '''if(p[0] == 'Normal'):
        print("\nSecondo me ste bun!")
    elif(p[0] == 'Anxiety'):
        print("\nSei ansioso frae!")
    elif (p[0] == 'Depression'):
       print("\nSei depresso bro!")
    elif (p[0] == 'Loneliness'):
       print("\nFra non sei solo non ti preoccupaere!")
    elif (p[0] == 'Stress'):
        print("\nFrae sei stresseto!")'''

    if (p[0] == 0):
        print("\nSecondo me ste bun!")
    elif (p[0] == 1):
        print("\nSei ansioso frae!")
    elif (p[0] == 2):
        print("\nSei depresso bro!")
    elif (p[0] == 3):
        print("\nFra non sei solo non ti preoccupaere!")
    elif (p[0] == 4):
        print("\nFrae sei stresseto!")
pass