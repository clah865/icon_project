'''
@author: Massaro, Trotti & Marino
'''
 
from user import User

def interaction():
    print("Benvenuto nel sistema per predire se sei affetto da disturbi mentali \n\
    Per capire cio' vi faremo una serie di domande su patologie pregresse e sintomi che potreste avere\n\
    Vi preghiamo di rispondere con la massima sincerita'\n\
    Grazie\n")
    print("Le risposte devono essere date nei possibili seguenti modi:\n\
    ->si-s-yes-y\n\
    ->no-n\n")
    utente = User()
    
    while(True):
        print('setHighBP?')
        utente.setHighBP(input(''))
        break

    while (True):
        print('setHighChol?')
        utente.setHighChol(input(''))
        break

    while (True):
        print('setCholCheck?')
        utente.setCholCheck(input(''))
        break

    while (True):
        print('BMI?')
        utente.setBMI(input(''))
        break

    while (True):
        print('setSmoker?')
        utente.setSmoker(input(''))
        break

    while (True):
        print('setStroke?')
        utente.setStroke(input(''))
        break

    while (True):
        print('setDiabetes?')
        utente.setDiabetes(input(''))
        break

    while (True):
        print('setPhysActivity?')
        utente.setPhysActivity(input(''))
        break

    while (True):
        print('setFruits?')
        utente.setFruits(input(''))
        break

    while (True):
        print('setVeggies?')
        utente.setVeggies(input(''))
        break

    while (True):
        print('setHvyAlcoholConsump?')
        utente.setHvyAlcoholConsump(input(''))
        break

    while (True):
        print('setAnyHealthcare?')
        utente.setAnyHealthcare(input(''))
        break

    while (True):
        print('setNoDocbcCost?')
        utente.setNoDocbcCost(input(''))
        break

    while (True):
        print('setGenHlth?')
        utente.setGenHlth(input(''))
        break

    while (True):
        print('setMentHlth?')
        utente.setMentHlth(input(''))
        break

    while (True):
        print('setPhysHlth?')
        utente.setPhysHlth(input(''))
        break

    while (True):
        print('setDiffWalk?')
        utente.setDiffWalk(input(''))
        break

    while (True):
        print('setSex?')
        utente.setSex(input(''))
        break

    while (True):
        print('setAge?')
        utente.setAge(input(''))
        break

    while (True):
        print('setEducation?')
        utente.setEducation(input(''))
        break

    while (True):
        print('setIncome?')
        utente.setIncome(input(''))
        break

    return utente