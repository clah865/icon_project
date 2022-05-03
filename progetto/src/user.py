'''
@author: Massaro, Trotti & Marino
'''

import pandas as pd

class User(object):

    def __init__(self):
        self.highBP = "No"
        self.highChol = "No"
        self.cholCheck = "No"
        self.BMI = "No"
        self.smoker = "No"
        self.stroke = "No"
        self.diabetes = "No"
        self.physActivity = "No"
        self.fruits = "No"
        self.veggies = "No"
        self.hvyAlcoholConsump = "No"
        self.genHlth = "No"
        #self.mentHlth = "No"
        #self.physHlth = "No"
        self.diffWalk = "No"
        self.sex = "No"
        self.age = "No"

        
    def getValues(self):
        df = pd.DataFrame.from_dict(vars(self), orient='index', dtype='string')
        return df

    def setHighBP(self, val):
        self.HighBP = val

    def setHighChol(self, val):
        self.HighChol = val

    def setCholCheck(self, val):
        self.CholCheck = val

    def setBMI(self, val):
        self.BMI = val

    def setSmoker(self, val):
        self.smoker = val

    def setStroke(self, val):
        self.stroke = val

    def setDiabetes(self, val):
        self.Diabetes = val

    def setPhysActivity(self, val):
        self.PhysActivity = val

    def setFruits(self, val):
        self.Fruits = val

    def setVeggies(self, val):
        self.Veggies = val

    def setHvyAlcoholConsump(self, val):
        self.HvyAlcoholConsump = val

    def setGenHlth(self, val):
        self.GenHlth = val

    def setMentHlth(self, val):
        self.MentHlth = val

    def setPhysHlth(self, val):
        self.PhysHlth = val

    def setDiffWalk(self, val):
        self.DiffWalk = val

    def setSex(self, val):
         self.sex = val

    def setAge(self, val):
        self.age = val



