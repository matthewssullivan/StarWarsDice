# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 20:49:11 2018
Star wars Dice App
Matt Sullivan
@author: oneey_000
"""

from random import randint
from random import seed
import numpy as np
seed()

class dice:
    value=None
    def __init__(self):
        self.value
        
#    def __repr__(self):
#        return self.value
#        
#    def __str__(self):
#        return str(self.value)
        
    def roll(self):
        newVal= randint(0,9)
        self.value = newVal
        return newVal
        
#    def roll(self, numSides):
#        newVal= randint(0, numSides-1)
#        self.value= newVal
#        return newVal

    def translateVector(self,abilityVector):
        print("D10 resuts:")
        for i in abilityVector:
            print(i)
#        print("Ability Dice Result: " + str(runningTally[0]) + " Success, " + str(runningTally[1]) + " Advantage.")
        return abilityVector
        
    def translateResult(self, results):
        print()
        print("Total Die Results:")
        if results[0]>=0:
            print(str(results[0]) + " Success")
        else:
            print(str(abs(results[0])) + " Failure")
        if results[1]>0:
            print(str(results[1]) + " Advantage")
        else:
            if results[1]<0:
                print(str(abs(results[1])) + " Threat")
        if results[2]>0:
            print(str(results[2]) + " Triumph")
        if results[3]<0:
            print(str(abs(results[3])) + " Despair")
        if results[4]>0:
            print(str(results[4]) + " Light side points")
        if results[5]>0:
            print(str(results[5]) + " Dark side points")
        
    def rollVector(self,numAbility):
        resultsVector=[]
        for i in range(numAbility):
            resultsVector.append(self.roll())
        return resultsVector
        
    def rollnum(self, number):
        vec=self.rollVector(number)
        return self.translateVector(vec)
        
    def totalAll(self,resultVec):
        endResult=(0,0,0,0,0,0)
        for i in resultVec:
            endResult = tuple(np.add(i,endResult))
        return endResult
        


class proficiency(dice):
    value = (0,0,0)
    def __init__(self):
        self.value=(0,0,0,0,0,0)
        
    def roll(self):
        newVal= randint(0,11)
        if newVal==(0 or 1):
            self.value = (2,0,0,0,0,0)
        if newVal== (2 or 3):
            self.value = (0,2,0,0,0,0)
        if newVal in (4,5,6):
            self.value=(1,1,0,0,0,0)
        if newVal==7:
            self.value=(0,1,0,0,0,0)
        if newVal==(8 or 9):
            self.value=(1,0,0,0,0,0)
        if newVal==10:
            self.value=(0,0,0,0,0,0)
        if newVal==11:
            self.value=(1,0,1,0,0,0)
        return self.value   
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Proficiency Dice Result: " + str(runningTally[0]) + " Success, " + str(runningTally[1]) + " Advantage," + str(runningTally[2]) + " Triumph" )
        return runningTally
    

class ability(dice):
    value = (0,0,0,0,0,0)
    
    def roll(self):
        newVal= randint(0,7)
        if newVal==(0 or 1):
            self.value = (1,0,0,0,0,0)
        if newVal== (2 or 3):
            self.value = (0,1,0,0,0,0)
        if newVal==4:
            self.value=(1,1,0,0,0,0)
        if newVal==5:
            self.value=(2,0,0,0,0,0)
        if newVal==6:
            self.value=(0,2,0,0,0,0)
        if newVal==7:
            self.value=(0,0,0,0,0,0)
        return self.value
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Ability Dice Result: " + str(runningTally[0]) + " Success, " + str(runningTally[1]) + " Advantage" )
        return runningTally
        
class difficulty(dice):
    value = (0,0,0,0,0,0)
    
    def roll(self):
        newVal= randint(0,7)
        if newVal==(0 or 1 or 2):
            self.value = (0,-1,0,0,0,0)
        if newVal== 3:
            self.value = (-1,-1,0,0,0,0)
        if newVal==4:
            self.value=(0,-2,0,0,0,0)
        if newVal==5:
            self.value=(-1,0,0,0,0,0)
        if newVal==6:
            self.value=(-2,0,0,0,0,0)
        if newVal==7:
            self.value=(0,0,0,0,0,0)
        return self.value
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Difficulty Dice Result: " + str(abs(runningTally[0])) + " Failure, " + str(abs(runningTally[1])) + " Threat")
        return runningTally

class challenge(dice):
    value = (0,0,0,0,0,0)
    def __init__(self):
        self.value=(0,0,0,0,0,0)
        
    def roll(self):
        newVal= randint(0,11)
        if newVal==(0 or 1):
            self.value = (-2,0,0,0,0,0)
        if newVal== (2 or 3):
            self.value = (0,-2,0,0,0,0)
        if newVal==(4 or 5):
            self.value=(-1,-1,0,0,0,0)
        if newVal==(6 or 7):
            self.value=(0,-1,0,0,0,0)
        if newVal==(8 or 9):
            self.value=(-1,0,0,0,0,0)
        if newVal==10:
            self.value=(0,0,0,0,0,0)
        if newVal==11:
            self.value=(-1,0,0,-1,0,0)
        return self.value   
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Challenge Dice Result: " + str(abs(runningTally[0])) + " Failure, " + str(abs(runningTally[1])) + " Threat," + str(abs(runningTally[3])) + " Despair" )
        return runningTally
        
class boost(dice):
    value = (0,0,0,0,0,0)
    
    def roll(self):
        newVal= randint(0,5)
        if newVal==(0 or 1):
            self.value = (0,0,0,0,0,0)
        if newVal== 2:
            self.value = (1,1,0,0,0,0)
        if newVal==3:
            self.value=(0,1,0,0,0,0)
        if newVal==4:
            self.value=(1,0,0,0,0,0)
        if newVal==5:
            self.value=(0,2,0,0,0,0)
        return self.value
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Boost Dice Result: " + str(runningTally[0]) + " Success, " + str(runningTally[1]) + " Advantage" )
        return runningTally
        
class setback(dice):
    value = (0,0,0,0,0,0)
    
    def roll(self):
        newVal= randint(0,5)
        if newVal==(0 or 1):
            self.value = (-1,0,0,0,0,0)
        if newVal== (2 or 3):
            self.value = (0,-1,0,0,0,0)
        if newVal==(4 or 5):
            self.value=(0,0,0,0,0,0)
        return self.value
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Setback Dice Result: " + str(abs(runningTally[0])) + " Failure, " + str(abs(runningTally[1])) + " Threat" )
        return runningTally
        
class force(dice):
    value = (0,0,0,0,0,0)
    
    def roll(self):
        newVal= randint(0,11)
        if newVal in (0,1,2,3,4,5):
            self.value = (0,0,0,0,0,1)
        if newVal in (6,7):
            self.value = (0,0,0,0,1,0)
        if newVal in (8,9,10):
            self.value=(0,0,0,0,2,0)
        if newVal==11:
            self.value=(0,0,0,0,0,2)
        return self.value
        
    def translateVector(self,abilityVector):
        runningTally=(0,0,0,0,0,0)
        for i in abilityVector:
            runningTally = tuple(np.add(i,runningTally))
        print("Force Dice Result: " + str(runningTally[4]) + " Light, " + str(runningTally[5]) + " Dark" )
        return runningTally


newAbility = ability()
newProf=proficiency()
newDiff=difficulty()
newChal=challenge()
newSetback=setback()
newBoost=boost()
newForce=force()

#vec = newAbility.rollVector(3)
#result=newAbility.translateVector(vec)
#
#
#vec2 = newProf.rollVector(3)
#result2=newProf.translateVector(vec2)
#
#vec3 =newDiff.rollVector(3)
#result3=newDiff.translateVector(vec3)
#
#vec4 = newChal.rollVector(4)
#result4=newChal.translateVector(vec4)

abilityRollNum=1
profRollNum=2
diffRollNum=2
chalRollNum=1
setbackRollNum=1
boostRollNum=2
forceRollNum=2

print("Rolling: " + str(abilityRollNum) + " Ability, " + str(profRollNum) + " Proficiency, " + str(diffRollNum) + " Difficulty " + str(chalRollNum) +" Challenge, " + str(boostRollNum) + " Boost " + str(setbackRollNum) + " Setback " + str(forceRollNum) + " Force dice" +"\n")


result = newAbility.rollnum(abilityRollNum)
result2= newProf.rollnum(profRollNum)
result3= newDiff.rollnum(diffRollNum)
result4= newChal.rollnum(chalRollNum)
result5= newSetback.rollnum(setbackRollNum)
result6= newBoost.rollnum(boostRollNum)
result7= newForce.rollnum(forceRollNum)

newList = (result, result2, result3, result4, result5, result6, result7)

next=newAbility.totalAll(newList)

newAbility.translateResult(next)
        

            
