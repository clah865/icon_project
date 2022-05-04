'''
@author: Massaro, Trotti & Marino
'''

import pandas as pd

class User(object):

    def __init__(self):
        self.highBP = 0
        self.highChol = 0
        self.cholCheck = 0
        self.BMI = 0
        self.smoker = 0
        self.stroke = 0
        self.diabetes = 0
        self.physActivity = 0
        self.fruits = 0
        self.veggies = 0
        self.hvyAlcoholConsump = 0
        self.genHlth = 0
        self.mentHlth = 0
        self.physHlth = 0
        self.diffWalk = 0
        self.sex = 0
        self.age = 0


    def getValues(self):
        df = pd.DataFrame.from_dict(vars(self), orient='index', dtype='string')
        return df

    def setHighBP(self, val):
        self.highBP = val

    def setHighChol(self, val):
        self.highChol = val

    def setCholCheck(self, val):
        self.cholCheck = val

    def setBMI(self, val):
        self.BMI = val

    def setSmoker(self, val):
        self.smoker = val

    def setStroke(self, val):
        self.stroke = val

    def setDiabetes(self, val):
        self.diabetes = val

    def setPhysActivity(self, val):
        self.physActivity = val

    def setFruits(self, val):
        self.fruits = val

    def setVeggies(self, val):
        self.veggies = val

    def setHvyAlcoholConsump(self, val):
        self.hvyAlcoholConsump = val

    def setGenHlth(self, val):
        self.genHlth = val

    def setMentHlth(self, val):
        self.mentHlth = val

    def setPhysHlth(self, val):
        self.physHlth = val

    def setDiffWalk(self, val):
        self.diffWalk = val

    def setSex(self, val):
         self.sex = val

    def setAge(self, val):
        self.age = val
