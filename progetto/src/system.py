'''
@author: Massaro, Trotti & Marino
'''

from model_performance import accuracy, MAE, kfold
import pandas as pd
from warnings import simplefilter
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from request import interaction
from prolog import ospedalization
import bayes as bay

if __name__ == '__main__':
    simplefilter(action='ignore', category=FutureWarning)

    data = pd.read_csv(r".\..\dataset\HeartDiseaseHealthIndicators.csv")
    
    y = data.HeartDiseaseorAttack
    x = data.drop('HeartDiseaseorAttack', axis=1)

    y=y.astype('int')
    x=x.astype('int')

    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    model = GradientBoostingClassifier()

    model.fit(x_train, y_train)
    p_train = model.predict(x_train)
    p_test = model.predict(x_test)

    '''accuracy(y_train, y_test, p_train, p_test)
    MAE(y_train, y_test, p_train, p_test)
    kfold(model, x, y)'''
    
    us = interaction()
    ris = us.getValues()

    risT = ris.T
    
    p = model.predict(risT)

    if(p[0] == 1):
        print("\nSecondo i dati analizzati, potresti soffrire di una malattia cardiaca.")
    elif(p[0] == 0):
        print("\nSecondo i dati analizzati, dovresti godere di buona salute.")

    ospedalization(ris)

    if(int(ris[0][12]) > 14):
        print("\nIl sistema ha rilevato che negli ultimi 30 giorni la tua salute mentale non è stata buona"
              "\nIl sistema è in grado di rilevare la percentuale della tua stabilità mentale")
        while(True):
            print("Vuoi utilizzare questa funzione? [s-n]")
            risposta = (input(''))
            if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
                bay.prediction()
                break
            elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
                print("Va bene... prova a consultare uno specialista!")
                break


pass