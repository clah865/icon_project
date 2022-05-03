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
    
    data = pd.read_csv(r".\..\dataset\heart_disease_health_indicators_BRFSS2015.csv")
    
    y = data.HeartDiseaseorAttack
    x = data.drop('HeartDiseaseorAttack', axis=1)

    y=y.astype('float')
    x=x.astype('float')

    x_train, x_test, y_train, y_test = train_test_split(x, y) #, test_size=0.2
    
    model = DecisionTreeClassifier()

    model.fit(x_train, y_train)    
    p_train = model.predict(x_train)
    p_test = model.predict(x_test)

    accuracy(y_train, y_test, p_train, p_test)
    MAE(y_train, y_test, p_train, p_test)
    kfold(model, x, y)
    
    us = interaction()
    ris = us.getValues()
    print ("\nRisultati");
    print(ris);
    #inserire qui la visualizzazione dei risultati e capisci
    #ospedalization(ris)
    
    for index, row in ris.iterrows():
        if(row[0] == 'Yes'):
            row[0]=1
        else:
            row[0]=0
    ris = ris.T
    
    p = model.predict(ris)
    print("\nRisultato predizione");
    print(p);
    if(p[0] == 1):
        print("\nSecondo me tu si matt!")
    elif(p[0] == 0):
        print("\nSecondo me ste bun!")
    else: (print("\nciao"))
        
pass