'''
@author: Massaro, Trotti & Marino
'''

import pandas as pd

class User(object):

    def __init__(self):
        self.HighBP = "No"
        self.HighChol = "No"
        self.CholCheck = "No"
        self.BMI = "No"
        self.smoker = "No"
        self.stroke = "No"
        self.Diabetes = "No"
        self.PhysActivity = "No"
        self.Fruits = "No"
        self.Veggies = "No"
        self.HvyAlcoholConsump = "No"
        self.AnyHealthcare = "No"
        self.NoDocbcCost= "No"
        self.GenHlth = "No"
        self.MentHlth = "No"
        self.PhysHlth = "No"
        self.Diabetes = "No"
        self.PhysActivity = "No"
        self.DiffWalk = "No"
        self.sex = "No"
        self.age = "No"
        self.Education = "No"
        self.Income = "No"


        
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

    def setAnyHealthcare(self, val):
        self.AnyHealthcare = val

    def setNoDocbcCost(self, val):
        self.NoDocbcCost = val

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

    def setEducation(self, val):
        self.Education = val

    def setIncome(self, val):
        self.Income = val
        


