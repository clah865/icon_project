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
        print('Ti senti nervoso?')
        utente.setFeelingNervous(input(''))
        if(utente.feelingNervous.lower().__eq__('si') or utente.feelingNervous.lower().__eq__('s') or utente.feelingNervous.lower().__eq__('y') or utente.feelingNervous.lower().__eq__('yes')):
            utente.setFeelingNervous('Yes')
            break
        elif(utente.feelingNervous.lower().__eq__('no') or utente.feelingNervous.lower().__eq__('n')):
            utente.setFeelingNervous('No')
            break
        
    while(True): 
        print("Hai attacchi di panico?")
        utente.setPanic(input(''))
        if(utente.panic.lower().__eq__('si') or utente.panic.lower().__eq__('s') or utente.panic.lower().__eq__('y') or utente.panic.lower().__eq__('yes')):
            utente.setPanic('Yes')
            break
        elif(utente.panic.lower().__eq__('no') or utente.panic.lower().__eq__('n')):
            utente.setPanic('No')
            break
    
    while(True):
        print("Hai iperventilazione?")
        utente.setBreathingRapidly(input(''))
        if(utente.breathingRapidly.lower().__eq__('si') or utente.breathingRapidly.lower().__eq__('s') or utente.breathingRapidly.lower().__eq__('y') or utente.breathingRapidly.lower().__eq__('yes')):
            utente.setBreathingRapidly('Yes')
            break
        elif(utente.breathingRapidly.lower().__eq__('no') or utente.breathingRapidly.lower().__eq__('n')):
            utente.setBreathingRapidly('No')
            break
        
    while(True):
        print("Stai sudando?")
        utente.setSweating(input(''))
        if(utente.sweating.lower().__eq__('si') or utente.sweating.lower().__eq__('s') or utente.sweating.lower().__eq__('y') or utente.sweating.lower().__eq__('yes')):
            utente.setSweating('Yes')
            break
        elif(utente.sweating.lower().__eq__('no') or utente.sweating.lower().__eq__('n')):
            utente.setSweating('No')
            break
        
    while(True):    
        print("Hai problemi di concentrazione?")
        utente.setTroubleInConcentration(input(''))
        if(utente.troubleInConcentration.lower().__eq__('si') or utente.troubleInConcentration.lower().__eq__('s') or utente.troubleInConcentration.lower().__eq__('y') or utente.troubleInConcentration.lower().__eq__('yes')):
            utente.setTroubleInConcentration('Yes')
            break
        elif(utente.troubleInConcentration.lower().__eq__('no') or utente.troubleInConcentration.lower().__eq__('n')):
            utente.setTroubleInConcentration('No')
            break
     
    while(True):    
        print("Hai problemi a dormire?")
        utente.setHavingTroubleInSleeping(input(''))
        if(utente.havingTroubleInSleeping.lower().__eq__('si') or utente.havingTroubleInSleeping.lower().__eq__('s') or utente.havingTroubleInSleeping.lower().__eq__('y') or utente.havingTroubleInSleeping.lower().__eq__('yes')):
            utente.setHavingTroubleInSleeping('Yes')
            break
        elif(utente.havingTroubleInSleeping.lower().__eq__('no') or utente.havingTroubleInSleeping.lower().__eq__('n')):
            utente.setHavingTroubleInSleeping('No')
            break
        
    while(True):
        print("Hai problemi a lavoro?")
        utente.setHavingTroubleWithWork(input(''))
        if(utente.havingTroubleWithWork.lower().__eq__('si') or utente.havingTroubleWithWork.lower().__eq__('s') or utente.havingTroubleWithWork.lower().__eq__('y') or utente.havingTroubleWithWork.lower().__eq__('yes')):
            utente.setHavingTroubleWithWork('Yes')
            break
        elif(utente.havingTroubleWithWork.lower().__eq__('no') or utente.havingTroubleWithWork.lower().__eq__('n')):
            utente.setHavingTroubleWithWork('No')
            break
        
    while(True):
        print("Hai mancanza di speranza?")
        utente.setHopelessness(input(''))
        if(utente.hopelessness.lower().__eq__('si') or utente.hopelessness.lower().__eq__('s') or utente.hopelessness.lower().__eq__('y') or utente.hopelessness.lower().__eq__('yes')):
            utente.setHopelessness('Yes')
            break
        elif(utente.hopelessness.lower().__eq__('no') or utente.hopelessness.lower().__eq__('n')):
            utente.setHopelessness('No')
            break

    while (True):
        print("Ti senti rabbioso?")
        utente.setAnger(input(''))
        if (utente.anger.lower().__eq__('si') or utente.anger.lower().__eq__('s') or utente.anger.lower().__eq__(
            'y') or utente.anger.lower().__eq__('yes')):
            utente.setAnger('Yes')
            break
        elif (utente.anger.lower().__eq__('no') or utente.anger.lower().__eq__('n')):
            utente.setAnger('No')
            break

    while (True):
        print("Hai reazioni esagerate?")
        utente.setOverReact(input(''))
        if (utente.overReact.lower().__eq__('si') or utente.overReact.lower().__eq__('s') or utente.overReact.lower().__eq__(
            'y') or utente.overReact.lower().__eq__('yes')):
            utente.setOverReact('Yes')
            break
        elif (utente.overReact.lower().__eq__('no') or utente.overReact.lower().__eq__('n')):
            utente.setOverReact('No')
            break

    while (True):
        print("Hai cambiato abitudini alimentari?")
        utente.setChangeInEating(input(''))
        if (utente.changeInEating.lower().__eq__('si') or utente.changeInEating.lower().__eq__(
            's') or utente.changeInEating.lower().__eq__('y') or utente.changeInEating.lower().__eq__('yes')):
            utente.setChangeInEating('Yes')
            break
        elif (utente.changeInEating.lower().__eq__('no') or utente.changeInEating.lower().__eq__('n')):
            utente.setChangeInEating('No')
            break

    while (True):
        print("Hai mai pensato di suicidarti? (se la risposta e' no fallo)")
        utente.setSuicidalThought(input(''))
        if (utente.suicidalThought.lower().__eq__('si') or utente.suicidalThought.lower().__eq__(
            's') or utente.suicidalThought.lower().__eq__('y') or utente.suicidalThought.lower().__eq__('yes')):
            utente.setSuicidalThought('Yes')
            break
        elif (utente.suicidalThought.lower().__eq__('no') or utente.suicidalThought.lower().__eq__('n')):
            utente.setSuicidalThought('No')
            break

    while (True):
        print("Ti senti stanco?")
        utente.setFeelingTired(input(''))
        if (utente.feelingTired.lower().__eq__('si') or utente.feelingTired.lower().__eq__(
            's') or utente.feelingTired.lower().__eq__('y') or utente.feelingTired.lower().__eq__('yes')):
            utente.setFeelingTired('Yes')
            break
        elif (utente.feelingTired.lower().__eq__('no') or utente.feelingTired.lower().__eq__('n')):
            utente.setFeelingTired('No')
            break

    while (True):
        print("Hai poki amici?")
        utente.setCloseFriend(input(''))
        if (utente.closeFriend.lower().__eq__('si') or utente.closeFriend.lower().__eq__(
            's') or utente.closeFriend.lower().__eq__('y') or utente.closeFriend.lower().__eq__('yes')):
            utente.setCloseFriend('Yes')
            break
        elif (utente.closeFriend.lower().__eq__('no') or utente.closeFriend.lower().__eq__('n')):
            utente.setCloseFriend('No')
            break

    while (True):
        print("Sei attivo sui social?")
        utente.setSocialMediaAddiction(input(''))
        if (utente.socialMediaAddiction.lower().__eq__('si') or utente.socialMediaAddiction.lower().__eq__(
            's') or utente.socialMediaAddiction.lower().__eq__(
            'y') or utente.socialMediaAddiction.lower().__eq__('yes')):
            utente.setSocialMediaAddiction('Yes')
            break
        elif (utente.socialMediaAddiction.lower().__eq__('no') or utente.socialMediaAddiction.lower().__eq__('n')):
            utente.setSocialMediaAddiction('No')
            break

    while (True):
        print("Sei aumentato di peso?")
        utente.setWeightGain(input(''))
        if (utente.weightGain.lower().__eq__('si') or utente.weightGain.lower().__eq__(
            's') or utente.weightGain.lower().__eq__('y') or utente.weightGain.lower().__eq__('yes')):
            utente.setWeightGain('Yes')
            break
        elif (utente.weightGain.lower().__eq__('no') or utente.weightGain.lower().__eq__('n')):
            utente.setWeightGain('No')
            break

    while(True):
        print("Sei possessivo verso ciò che è tuo?")
        utente.setMaterialPossessions(input(''))
        if(utente.materialPossessions.lower().__eq__('si') or utente.materialPossessions.lower().__eq__('s') or utente.materialPossessions.lower().__eq__('y') or utente.materialPossessions.lower().__eq__('yes')):
            utente.setMaterialPossessions('Yes')
            break
        elif(utente.materialPossessions.lower().__eq__('no') or utente.materialPossessions.lower().__eq__('n')):
            utente.setMaterialPossessions('No')
            break
         
    while(True):
        print("Sei introverso?")
        utente.setIntrovert(input(''))
        if(utente.introvert.lower().__eq__('si') or utente.introvert.lower().__eq__('s') or utente.introvert.lower().__eq__('y') or utente.introvert.lower().__eq__('yes')):
            utente.setIntrovert('Yes')
            break
        elif(utente.introvert.lower().__eq__('no') or utente.introvert.lower().__eq__('n')):
            utente.setIntrovert('No')
            break
        
    while(True):
        print("Spesso ti ricordi di momenti stressanti?")
        utente.setPoppingUpStressfulMemory(input(''))
        if(utente.poppingUpStressfulMemory.lower().__eq__('si') or utente.poppingUpStressfulMemory.lower().__eq__('s') or utente.poppingUpStressfulMemory.lower().__eq__('y') or utente.poppingUpStressfulMemory.lower().__eq__('yes')):
            utente.setPoppingUpStressfulMemory('Yes')
            break
        elif(utente.poppingUpStressfulMemory.lower().__eq__('no') or utente.poppingUpStressfulMemory.lower().__eq__('n')):
            utente.setPoppingUpStressfulMemory('No')
            break
        
    while(True):
        print("Hai incubi?")
        utente.setHavingNightmares(input(''))
        if(utente.havingNightmares.lower().__eq__('si') or utente.havingNightmares.lower().__eq__('s') or utente.havingNightmares.lower().__eq__('y') or utente.havingNightmares.lower().__eq__('yes')):
            utente.setHavingNightmares('Yes')
            break
        elif(utente.havingNightmares.lower().__eq__('no') or utente.havingNightmares.lower().__eq__('n')):
            utente.setHavingNightmares('No')
            break

    while (True):
        print("Ti sei allontanato da persone o attività?")
        utente.setAvoidsPeopleOrActivities(input(''))
        if (utente.avoidsPeopleOrActivities.lower().__eq__('si') or utente.avoidsPeopleOrActivities.lower().__eq__(
                's') or utente.avoidsPeopleOrActivities.lower().__eq__('y') or utente.avoidsPeopleOrActivities.lower().__eq__('yes')):
            utente.setAvoidsPeopleOrActivities('Yes')
            break
        elif (utente.avoidsPeopleOrActivities.lower().__eq__('no') or utente.avoidsPeopleOrActivities.lower().__eq__('n')):
            utente.setAvoidsPeopleOrActivities('No')
            break

    while (True):
        print("Ti senti negativo?")
        utente.setFeelingNegative(input(''))
        if (utente.feelingNegative.lower().__eq__('si') or utente.feelingNegative.lower().__eq__(
                's') or utente.feelingNegative.lower().__eq__('y') or utente.feelingNegative.lower().__eq__('yes')):
            utente.setFeelingNegative('Yes')
            break
        elif (utente.feelingNegative.lower().__eq__('no') or utente.feelingNegative.lower().__eq__('n')):
            utente.setFeelingNegative('No')
            break

    while (True):
        print("Hai problemi a concentrarti?")
        utente.setTroubleConcentrating(input(''))
        if (utente.troubleConcentrating.lower().__eq__('si') or utente.troubleConcentrating.lower().__eq__(
                's') or utente.troubleConcentrating.lower().__eq__('y') or utente.troubleConcentrating.lower().__eq__('yes')):
            utente.setTroubleConcentrating('Yes')
            break
        elif (utente.troubleConcentrating.lower().__eq__('no') or utente.troubleConcentrating.lower().__eq__('n')):
            utente.setTroubleConcentrating('No')
            break

    while (True):
        print("Ti incolpi spesso?")
        utente.setBlamingYourself(input(''))
        if (utente.blamingYourself.lower().__eq__('si') or utente.blamingYourself.lower().__eq__(
                's') or utente.blamingYourself.lower().__eq__('y') or utente.blamingYourself.lower().__eq__('yes')):
            utente.setBlamingYourself('Yes')
            break
        elif (utente.blamingYourself.lower().__eq__('no') or utente.blamingYourself.lower().__eq__('n')):
            utente.setBlamingYourself('No')
            break
  
    return utente