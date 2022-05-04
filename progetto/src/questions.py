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
        risposta = (input(''))
        if (risposta.lower().__eq__('m') or risposta.lower().__eq__('maschio') or risposta.lower().__eq__('male')):
            utente.setSex(1)
            flag = 1
            break
        elif (risposta.lower().__eq__('f') or risposta.__eq__('femmina') or risposta.lower().__eq__('female')):
            utente.setSex(0)
            flag = 0
            break

    while (True):
        print('Hai una pressione sanguigna elevata?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setHighBP(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHighBP(0)
            break

    while (True):
        print('Ti è mai stato detto da un medico, un infermiere o un altro operatore sanitario che il tuo colesterolo nel sangue è alto?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setHighChol(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHighChol(0)
            break

    while (True):
        print('Hai eseguito un controllo del colesterolo negli ultimi cinque anni?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setCholCheck(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setCholCheck(0)
            break

    while (True):
        print('Qual è il tuo indice di massa corporea(BMI)?')
        utente.setBMI(input(''))
        break

    while (True):
        print('Hai fumato almeno 100 sigarette in tutta la tua vita?[Nota: 5 pacchetti = 100 sigarette]')
        risposta = (input(''))
        if (risposta.__eq__('si') or risposta.__eq__('s') or risposta.__eq__('y') or risposta.__eq__('yes')):
            utente.setSmoker(1)
            break
        elif (risposta.__eq__('no') or risposta.__eq__('n')):
            utente.setSmoker(0)
            break

    while (True):
        print('Hai mai avuto un ictus?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setStroke(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setStroke(0)
            break


    while (True):
        print('Hai il diabete?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setDiabetes(2)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setDiabetes(0)
            if (flag == 0):
                print('Hai avuto il diabete solo durante la gravidanza?')
                utente.setDiabetes(input(''))
                if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                     's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
                    utente.setDiabetes(0)
                    break
                elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
                    utente.setDiabetes(0)

            print('Sei in uno stato di pre-diabete?')
            utente.setDiabetes(input(''))
            if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                    's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
                utente.setDiabetes(1)
                break
            elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
                utente.setDiabetes(0)
                break



    while (True):
        print('Hai svolto attività fisica o esercizio fisico negli ultimi 30 giorni in modo diverso dal normale lavoro?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setPhysActivity(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setPhysActivity(0)
            break

    while (True):
        print('Mangi frutta 1 o più volte al giorno? ')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setFruits(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setFruits(0)
            break

    while (True):
        print('Mangi verdura 1 o più volte al giorno? ')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setVeggies(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setVeggies(0)
            break

    while (True):
        if(flag == 1):
            print('Bevi più di 14 drink a settimana?')
        else:
            print('Bevi più di 7 drink a settimana?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or utente.risposta.lower().__eq__('yes')):
            utente.setHvyAlcoholConsump(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHvyAlcoholConsump(0)
            break

    while (True):
        print('Diresti che in genere la tua salute è (valore massimo 1, valore minimo 5):')
        risposta = (input(''))
        if (int(risposta) >= 1 and int(risposta) <= 5 ):
            utente.setGenHlth(risposta)
            break
        else:
            print('Valore non valido!')

    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute mentale non è stata buona?')
        risposta = (input(''))
        if (int(risposta) >= 0 and int(risposta) <= 30 ):
            utente.setMentHlth(input(''))
            break
        else:
            print('Valore non valido!')

    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute fisica non è stata buona?')
        risposta = (input(''))
        if (int(risposta) >= 0 and int(risposta) <= 30 ):
            utente.setPhysHlth(input(''))
            break
        else:
            print('Valore non valido!')

    while (True):
        print('Hai difficoltà nel camminare o nel salire le scale?')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setDiffWalk(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setDiffWalk(0)
            break

    while (True):
        print('Inserisci la tua eta:')
        risposta = (input(''))
        if (int(risposta) >= 18 and int(risposta) <= 24):
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