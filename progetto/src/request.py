'''
@author: Massaro, Trotti & Marino
'''
 
from user import User

def interaction():
    print("Benvenuto nel sistema per predire se sei affetto di una malattia cardiaca. \n\
    Per capire cio' verranno somministrate una serie di domande riguardanti il tuo stile di vita e il tuo stato psicofisico.\n\
    Ti è consigliato di rispondere con la massima serietà.'\n\
    Grazie.\n")

    print("La maggior parte delle domande richiederà risposte di questo tipo (ti verrà indicato quando):\n\
    ->si-s-yes-y\n\
    ->no-n\n")

    utente = User()

    #sesso
    while (True):
        print('Inserisci il tuo sesso [m/maschio/male][f/femmina/female]:')
        risposta = (input(''))
        if (risposta.lower().__eq__('m') or risposta.lower().__eq__('maschio') or risposta.lower().__eq__('male')):
            utente.setSex(1)
            flag = 1
            break
        elif (risposta.lower().__eq__('f') or risposta.__eq__('femmina') or risposta.lower().__eq__('female')):
            utente.setSex(0)
            flag = 0
            break


    # età
    while (True):
        print('Inserisci la tua eta:')
        risposta = (input(''))
        if (risposta.isdigit()):
            if (int(risposta) >= 18 and int(risposta) <= 24):
                utente.setAge(1)
                break
            elif (int(risposta) >= 25 and int(risposta) <= 29):
                utente.setAge(2)
                break
            elif (int(risposta) >= 30 and int(risposta) <= 34):
                utente.setAge(3)
                break
            elif (int(risposta) >= 35 and int(risposta) <= 39):
                utente.setAge(4)
                break
            elif (int(risposta) >= 40 and int(risposta) <= 44):
                utente.setAge(5)
                break
            elif (int(risposta) >= 45 and int(risposta) <= 49):
                utente.setAge(6)
                break
            elif (int(risposta) >= 50 and int(risposta) <= 54):
                utente.setAge(7)
                break
            elif (int(risposta) >= 55 and int(risposta) <= 59):
                utente.setAge(8)
                break
            elif (int(risposta) >= 60 and int(risposta) <= 64):
                utente.setAge(9)
                break
            elif (int(risposta) >= 65 and int(risposta) <= 69):
                utente.setAge(10)
                break
            elif (int(risposta) >= 70 and int(risposta) <= 74):
                utente.setAge(11)
                break
            elif (int(risposta) >= 75 and int(risposta) <= 79):
                utente.setAge(12)
                break
            elif (int(risposta) >= 80 and int(risposta)<= 120):
                utente.setAge(13)
                break
            elif (int(risposta) <= 17):
                print("L'intervistato è minorenne, è possibile utilizzare questo sistema solo se maggiorenne!")
                quit()
        else:
            print('Valore non valido')


    #pressione elevata
    while (True):
        print('Hai una pressione sanguigna elevata? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setHighBP(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHighBP(0)
            break

    #colesterolo alto
    while (True):
        print('Il tuo colesterolo nel sangue è elevato? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setHighChol(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHighChol(0)
            break

    #controllo colesterolo
    while (True):
        print('Hai eseguito un controllo del colesterolo negli ultimi cinque anni? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setCholCheck(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setCholCheck(0)
            break

    #BMI
    while (True):
        print("Qual è il tuo indice di massa corporea(BMI)? [arrotonda per eccesso o difetto al numero intero]")
        risposta = input('')
        if (risposta.isdigit()):
            if (int(risposta) >= 60 or int(risposta) <= 14):
                print('Hai indicato un valore BMI anormale')
            else:
                utente.setBMI(int(risposta))
                break
        else:
            print('Valore non valido')

    #fumo
    while (True):
        print('Hai fumato almeno 100 sigarette (5 pacchetti) in tutta la tua vita? [s-n]')
        risposta = (input(''))
        if (risposta.__eq__('si') or risposta.__eq__('s') or risposta.__eq__('y') or risposta.__eq__('yes')):
            utente.setSmoker(1)
            break
        elif (risposta.__eq__('no') or risposta.__eq__('n')):
            utente.setSmoker(0)
            break

    #ictus
    while (True):
        print('Hai mai avuto un ictus? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setStroke(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setStroke(0)
            break

    #diabete
    while (True):
        print('Hai il diabete? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setDiabetes(2)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setDiabetes(0)
            if (flag == 0):
                print('Hai avuto il diabete solo durante la gravidanza? [s-n]')
                utente.setDiabetes(input(''))
                if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                     's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
                    utente.setDiabetes(0)
                    break
                elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
                    utente.setDiabetes(0)

            print('Sei in uno stato di pre-diabete? [s-n]')
            utente.setDiabetes(input(''))
            if (risposta.lower().__eq__('si') or risposta.lower().__eq__(
                    's') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
                utente.setDiabetes(1)
                break
            elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
                utente.setDiabetes(0)
                break


    #attività fisica
    while (True):
        print('Hai svolto attività fisica o esercizio fisico negli ultimi 30 giorni in modo diverso dal normale lavoro? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setPhysActivity(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setPhysActivity(0)
            break

    #frutta
    while (True):
        print('Mangi frutta 1 o più volte al giorno?[s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setFruits(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setFruits(0)
            break

    #verdura
    while (True):
        print('Mangi verdura 1 o più volte al giorno? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setVeggies(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setVeggies(0)
            break

    #consumo alcool
    while (True):
        if(flag == 1):
            print('Bevi più di 14 drink a settimana? [s-n]')
        else:
            print('Bevi più di 7 drink a settimana? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setHvyAlcoholConsump(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setHvyAlcoholConsump(0)
            break

    #valore salute
    while (True):
        print('Indica, secondo te, il tuo stato di salute da 1 a 5 [valore massimo 1, valore minimo 5]:')
        risposta = (input(''))
        if (risposta.isdigit()):
            if (int(risposta) >= 1 and int(risposta) <= 5 ):
                utente.setGenHlth(risposta)
                break
            else:
                print('Valore non valido!')
        else:
            print('Valore non valido!')


    #salute mentale
    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute mentale non è stata buona? ')
        risposta = (input(''))
        if (risposta.isdigit()):
            if (int(risposta) >= 0 and int(risposta) <= 30 ):
                utente.setMentHlth(int(risposta))
                break
            else:
                print('Valore non valido!')
        else:
            print('Valore non valido!')


    #salute fisica
    while (True):
        print('Per quanti giorni negli ultimi 30 giorni la tua salute fisica non è stata buona?')
        risposta = (input(''))
        if (risposta.isdigit()):
            if (int(risposta) >= 0 and int(risposta) <= 30 ):
                utente.setPhysHlth(int(risposta))
                break
            else:
                print('Valore non valido!')
        else:
            print('Valore non valido!')

    #difficoltà camminare
    while (True):
        print('Hai difficoltà nel camminare o nel salire le scale? [s-n]')
        risposta = (input(''))
        if (risposta.lower().__eq__('si') or risposta.lower().__eq__('s') or risposta.lower().__eq__('y') or risposta.lower().__eq__('yes')):
            utente.setDiffWalk(1)
            break
        elif (risposta.lower().__eq__('no') or risposta.lower().__eq__('n')):
            utente.setDiffWalk(0)
            break



    return utente