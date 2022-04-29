'''
@author: Massaro, Trotti & Marino
'''

import pandas as pd

class User(object):

    def __init__(self):
        self.feelingNervous = "No"
        self.panic = "No"
        self.breathingRapidly = "No"
        self.sweating = "No"
        self.troubleInConcentration = "No"
        self.havingTroubleInSleeping = "No"
        self.havingTroubleWithWork = "No"
        self.hopelessness = "No"
        self.anger = "No"
        self.overReact = "No"
        self.changeInEating = "No"
        self.suicidalThought = "No"
        self.feelingTired = "No"
        self.closeFriend = "No"
        self.socialMediaAddiction = "No"
        self.weightGain = "No"
        self.materialPossessions = "No"
        self.introvert = "No"
        self.poppingUpStressfulMemory = "No"
        self.havingNightmares = "No"
        self.avoidsPeopleOrActivities = "No"
        self.feelingNegative = "No"
        self.troubleConcentrating = "No"
        self.blamingYourself = "No"

        
    def getValues(self):
        df = pd.DataFrame.from_dict(vars(self), orient='index', dtype='string')
        return df

    def setFeelingNervous(self, val):
        self.feelingNervous = val
     
    def setPanic(self, val):
        self.panic =val
      
    def setBreathingRapidly(self, val):
        self.breathingRapidly =val
        
    def setSweating(self, val):
        self.sweating =val
        
    def setTroubleInConcentration(self, val):
        self.troubleInConcentration =val
        
    def setHavingTroubleInSleeping(self, val):
        self.havingTroubleInSleeping =val
        
    def setHavingTroubleWithWork(self, val):
        self.havingTroubleWithWork =val
        
    def setHopelessness(self, val):
        self.hopelessness =val
        
    def setAnger(self, val):
        self.anger =val
        
    def setOverReact(self, val):
        self.overReact =val
       
    def setChangeInEating(self, val):
        self.changeInEating =val
        
    def setSuicidalThought(self, val):
        self.suicidalThought =val

    def setFeelingTired(self, val):
        self.feelingTired = val

    def setCloseFriend(self, val):
        self.closeFriend =val

    def setSocialMediaAddiction(self, val):
        self.socialMediaAddiction =val

    def setWeightGain(self, val):
        self.weightGain =val

    def setMaterialPossessions(self, val):
        self.materialPossessions =val

    def setIntrovert(self, val):
        self.introvert =val

    def setPoppingUpStressfulMemory(self, val):
        self.poppingUpStressfulMemory =val

    def setHavingNightmares(self, val):
        self.havingNightmares =val

    def setAvoidsPeopleOrActivities(self, val):
        self.avoidsPeopleOrActivities =val

    def setFeelingNegative(self, val):
        self.feelingNegative =val

    def setTroubleConcentrating(self, val):
        self.troubleConcentrating =val

    def setBlamingYourself(self, val):
        self.blamingYourself =val

