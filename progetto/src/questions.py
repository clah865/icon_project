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

    while (True):
        print('Inserisci il tuo sesso:')
        utente.setSex(input(''))
        if (utente.sex.lower().__eq__('m') or utente.sex.lower().__eq__('maschio') or utente.sex.lower().__eq__(
                'male')):
            utente.setSex(1)
            flag = 1
            break
        elif (utente.sex.lower().__eq__('f') or utente.sex.lower().__eq__('femmina') or utente.sex.lower().__eq__(
                'female')):
            utente.setSex(0)
            flag = 0
            break

    while (True):
        print('Hai una pressione sanguigna elevata?')
        utente.setHighBP(input(''))
        if (utente.highBP.lower().__eq__('si') or utente.highBP.lower().__eq__(
            's') or utente.highBP.lower().__eq__('y') or utente.highBP.lower().__eq__('yes')):
            utente.setHighBP('Yes')
            break
        elif (utente.highBP.lower().__eq__('no') or utente.highBP.lower().__eq__('n')):
            utente.setHighBP('No')
            break

    while (True):
        print('Ti è MAI stato detto da un medico, un infermiere o un altro operatore sanitario che il tuo colesterolo nel sangue è alto?')
        utente.setHighChol(input(''))
        if (utente.highChol.lower().__eq__('si') or utente.highChol.lower().__eq__(
                's') or utente.highChol.lower().__eq__('y') or utente.highChol.lower().__eq__('yes')):
            utente.setHighChol('Yes')
            break
        elif (utente.highChol.lower().__eq__('no') or utente.highChol.lower().__eq__('n')):
            utente.setHighChol('No')
            break

    while (True):
        print('Hai eseguito un controllo del colesterolo negli ultimi cinque anni?')
        utente.setCholCheck(input(''))
        if (utente.cholCheck.lower().__eq__('si') or utente.cholCheck.lower().__eq__(
                's') or utente.cholCheck.lower().__eq__('y') or utente.cholCheck.lower().__eq__('yes')):
            utente.setCholCheck('Yes')
            break
        elif (utente.cholCheck.lower().__eq__('no') or utente.cholCheck.lower().__eq__('n')):
            utente.setCholCheck('No')
            break

    while (True):
        print('Qual è il tuo indice di massa corporea(BMI)?')
        utente.setBMI(input(''))
        break

    while (True):
        print('Hai fumato almeno 100 sigarette in tutta la tua vita?[Nota: 5 pacchetti = 100 sigarette]')
        utente.setSmoker(input(''))
        if (utente.smoker.lower().__eq__('si') or utente.smoker.lower().__eq__(
                's') or utente.smoker.lower().__eq__('y') or utente.smoker.lower().__eq__('yes')):
            utente.setSmoker('Yes')
            break
        elif (utente.smoker.lower().__eq__('no') or utente.smoker.lower().__eq__('n')):
            utente.setSmoker('No')
            break

    while (True):
        print('Hai mai avuto un ictus?')
        utente.setStroke(input(''))
        if (utente.stroke.lower().__eq__('si') or utente.stroke.lower().__eq__(
                's') or utente.stroke.lower().__eq__('y') or utente.stroke.lower().__eq__('yes')):
            utente.setStroke('Yes')
            break
        elif (utente.stroke.lower().__eq__('no') or utente.stroke.lower().__eq__('n')):
            utente.setStroke('No')
            break


    while (True):
        print('Hai il diabete?')
        utente.setDiabetes(input(''))
        if (utente.diabetes.lower().__eq__('si') or utente.diabetes.lower().__eq__(
                's') or utente.diabetes.lower().__eq__('y') or utente.diabetes.lower().__eq__('yes')):
            utente.setDiabetes(2)
            break
        elif (utente.diabetes.lower().__eq__('no') or utente.diabetes.lower().__eq__('n')):
            utente.setDiabetes(0)
            if (flag == 0):
                print('Hai avuto il diabete solo durante la gravidanza?')
                utente.setDiabetes(input(''))
            if (utente.diabetes.lower().__eq__('si') or utente.diabetes.lower().__eq__(
                    's') or utente.diabetes.lower().__eq__('y') or utente.diabetes.lower().__eq__('yes')):
                utente.setDiabetes(0)
                break
            elif (utente.diabetes.lower().__eq__('no') or utente.diabetes.lower().__eq__('n')):
                utente.setDiabetes(0)

            print('Sei in pre-diabete?')
            utente.setDiabetes(input(''))
            if (utente.diabetes.lower().__eq__('si') or utente.diabetes.lower().__eq__(
                    's') or utente.diabetes.lower().__eq__('y') or utente.diabetes.lower().__eq__('yes')):
                utente.setDiabetes(1)
                break
            elif (utente.diabetes.lower().__eq__('no') or utente.diabetes.lower().__eq__('n')):
                utente.setDiabetes(0)
                break



    while (True):
        print('Hai svolto attività fisica o esercizio fisico negli ultimi 30 giorni in modo diverso dal normale lavoro?')
        utente.setPhysActivity(input(''))
        if (utente.physActivity.lower().__eq__('si') or utente.physActivity.lower().__eq__(
                's') or utente.physActivity.lower().__eq__('y') or utente.physActivity.lower().__eq__('yes')):
            utente.setPhysActivity('Yes')
            break
        elif (utente.physActivity.lower().__eq__('no') or utente.physActivity.lower().__eq__('n')):
            utente.setPhysActivity('No')
            break

    while (True):
        print('Mangi frutta 1 o più volte al giorno? ')
        utente.setFruits(input(''))
        if (utente.fruits.lower().__eq__('si') or utente.fruits.lower().__eq__(
                's') or utente.fruits.lower().__eq__('y') or utente.fruits.lower().__eq__('yes')):
            utente.setFruits('Yes')
            break
        elif (utente.fruits.lower().__eq__('no') or utente.fruits.lower().__eq__('n')):
            utente.setFruits('No')
            break

    while (True):
        print('Mangi verdura 1 o più volte al giorno? ')
        utente.setVeggies(input(''))
        if (utente.veggies.lower().__eq__('si') or utente.veggies.lower().__eq__(
                's') or utente.veggies.lower().__eq__('y') or utente.veggies.lower().__eq__('yes')):
            utente.setVeggies('Yes')
            break
        elif (utente.veggies.lower().__eq__('no') or utente.veggies.lower().__eq__('n')):
            utente.setVeggies('No')
            break

    while (True):
        if(flag == 1):
            print('Bevi più di 14 drink a settimana?')
        else:
            print('Bevi più di 7 drink a settimana?')
        utente.setHvyAlcoholConsump(input(''))
        if (utente.hvyAlcoholConsump.lower().__eq__('si') or utente.hvyAlcoholConsump.lower().__eq__(
                's') or utente.hvyAlcoholConsump.lower().__eq__('y') or utente.hvyAlcoholConsump.lower().__eq__('yes')):
            utente.setHvyAlcoholConsump('Yes')
            break
        elif (utente.hvyAlcoholConsump.lower().__eq__('no') or utente.hvyAlcoholConsump.lower().__eq__('n')):
            utente.setHvyAlcoholConsump('No')
            break

    while (True):
        print('Diresti che in genere la tua salute è (valore massimo 1, valore minimo 5):')
        utente.setGenHlth(input(''))
        if (utente.genHlth < 1 or utente.genHlth > 5 ):
            print('Valore non valido!')
        else:
            break

    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute mentale non è stata buona?')
        utente.setMentHlth(input(''))
        if (utente.mentHlth < 0 or utente.mentHlth > 30 ):
            print('Valore non valido!')
        else:
            break

    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute fisica non è stata buona?')
        utente.setPhysHlth(input(''))
        if (utente.physHlth < 0 or utente.physHlth > 30 ):
            print('Valore non valido!')
        else:
            break


    while (True):
        print('Hai difficoltà nel camminare o nel salire le scale?')
        utente.setDiffWalk(input(''))
        if (utente.diffWalk.lower().__eq__('si') or utente.diffWalk.lower().__eq__(
                's') or utente.diffWalk.lower().__eq__('y') or utente.diffWalk.lower().__eq__('yes')):
            utente.setDiffWalk('Yes')
            break
        elif (utente.diffWalk.lower().__eq__('no') or utente.diffWalk.lower().__eq__('n')):
            utente.setDiffWalk('No')
            break

    while (True):
        print('Inserisci la tua eta:')
        utente.setAge(input(''))
        if (utente.setAge >= 18 and utente.setAge <= 24):
            utente.setAge(1)
            break
        elif (utente.setAge >= 25 and utente.setAge <= 29):
            utente.setAge(2)
            break
        elif (utente.setAge >= 30 and utente.setAge <= 34):
            utente.setAge(3)
            break
        elif (utente.setAge >= 35 and utente.setAge <= 39):
            utente.setAge(4)
            break
        elif (utente.setAge >= 40 and utente.setAge <= 44):
            utente.setAge(5)
            break
        elif (utente.setAge >= 45 and utente.setAge <= 49):
            utente.setAge(6)
            break
        elif (utente.setAge >= 50 and utente.setAge <= 54):
            utente.setAge(7)
            break
        elif (utente.setAge >= 55 and utente.setAge <= 59):
            utente.setAge(8)
            break
        elif (utente.setAge >= 60 and utente.setAge <= 64):
            utente.setAge(9)
            break
        elif (utente.setAge >= 65 and utente.setAge <= 69):
            utente.setAge(10)
            break
        elif (utente.setAge >= 70 and utente.setAge <= 74):
            utente.setAge(11)
            break
        elif (utente.setAge >= 75 and utente.setAge <= 79):
            utente.setAge(12)
            break
        elif (utente.setAge >= 80):
            utente.setAge(13)
            break
        elif (utente.setAge <= 17):
            print('Intervistato è minorenne')
            quit()


    return utente