# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:42:32 2019

@author: Alexis Navarro
Olac Fuentes
CS 2302
Purpose: make a code to find if the equations are equal to each other and to use
backtracking to find the partition of the subset if possible.
"""

import random
import numpy as np
from math import *
import math
import time

       
#METHOD TO FIND IF THE EQUATIONS ARE EQUAL TO EACH OTHER
def equal(F):
    res=[] #LIST TO HOLD THE RESULTS
    t = random.uniform(-math.pi,math.pi)
    print('t=',t)
    for i in range(len(F)):
        for y in range(len(F)):
            y1 = eval(F[i]) 
            y2 = eval(F[y])
            if y1 == y2: # IF METHOD TO CHECK IF THE EQUATIONS ARE EQUAL
                res.append([F[i],F[y],True])
            else:
                res.append([F[i],F[y],False])
    return res

'''
#method to find the subsetSum of the equations to be used to see if they are equal.
def subsetSum(L,i,sumL):
    if sum ==0:
        return True
    if i == 0 and sum !=0:
        return False
    if L[i-1]>sum:
        return subsetSum(L,i-1,sum)
    return subsetSum(L,i-1,sum) or subsetSum(L,i-1,sum-L[i-1])
'''

# METHOD TO BACKTRACK 
def subsetsumP(S,last,goal):
    if goal ==0:
        return []
    if goal<0 or last<0:
        return []
    subset =[] # Take S[last]
    if S[last]>goal:
        return subsetsumP(S,last-1,goal)
    else:
        subset.append(S[last])
        return subsetsumP (S,last-1,goal) # Don't take S[last]

#METHOD TO FIND THE PARTITION OF THE SUBSETS
def partition(S,index):
    sumL=0
    for i in range(len(S)):
        sumL+=S[i]
    if sumL % 2 !=0: #IF THE SUM OF THE PASSED LIST IS NOT EVEN THEN THE TWO SUBSETS DON'T CAN'T BE EQUAL IN VALUE
        return False
    
    newList = subsetsumP(S,index,sumL//2)# the new list will hold the values that come from the subset sum 
    sum_newL=0
    sumRemL=0 #HOLDS THE SUM OF THE SUBLIST THAT IS NOT RETURNED
    rem=[]
    for j in range(len(S)): #INSERTS THE LIST WITH THE VALUES remaining from the new list
        if S[j] not in newList:
            rem.append(S[j])
    for k in range(len(newList)): # traverses the for loop to get the sum of the new list
        sum_newL += newList[k]
    for i2 in range(len(rem)): # gets the sum of the remaining list
        sumRemL += rem[i2]
    if sum_newL == sumL//2 and sumRemL==sumL//2:
        print(newList,rem)
    else:
        print('no sublist exist')
     

#------------------------------------------------------------------------------



#COMPARE THE EQUATIONS
F=['sin(t)','cos(t)','tan(t)','1/cos(t)','-sin(t)','cos(t)','-tan(t)','sin(-t)','cos(-t)','tan(-t)','sin(t)//cos(t)','2*sin(t/2)*2*cos(t/2)','sin(t)**2','1-cos(t)**2','(1-cos(2*t))/2','1/cos(t)']
results = equal(F)
for i in results:
    print(i)

#TEST THE PARTITIONS
#S = [2,4,5,9]
S=[2,4,5,9,12]
print(partition(S,len(S)-1))
    