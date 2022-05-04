'''
@author: Massaro, Trotti & Marino
'''

from model_performance import accuracy, MAE, kfold
import pandas as pd
from warnings import simplefilter
from sklearn.model_selection import train_test_split
from sklearn.tree._classes import DecisionTreeClassifier
from request import interaction

if __name__ == '__main__':
    simplefilter(action='ignore', category=FutureWarning)

    data = pd.read_csv(r".\..\dataset\heart_disease_health_indicators_BRFSS2022.csv")
    
    y = data.HeartDiseaseorAttack
    x = data.drop('HeartDiseaseorAttack', axis=1)

    y=y.astype('int')
    x=x.astype('int')

    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    model = DecisionTreeClassifier()

    model.fit(x_train, y_train)    
    p_train = model.predict(x_train)
    p_test = model.predict(x_test)

    accuracy(y_train, y_test, p_train, p_test)
    MAE(y_train, y_test, p_train, p_test)
    kfold(model, x, y)
    
    us = interaction()
    ris = us.getValues()

    ris = ris.T
    
    p = model.predict(ris)

    if(p[0] == 1):
        print("\nSecondo i dati analizzati, potresti soffrire di una malattia cardiaca. E consigliata una visita da uno specialista.")
    elif(p[0] == 0):
        print("\nSecondo i dati analizzati, dovresti godere di buona salute.")
        
pass