# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 14:50:22 2025

@author: USER
"""
R=1.1
print(input("enter the radius"))
Area=3.14*(R**2)
print(Area)
from math import pi
pi*(R**2)
#------------------------------------------------------#
fnmae=input("eneter the first name")
lname=input("enter the last name")
print(fnmae, " " ,lname )
print(lname ," ", fnmae)

#---------------------------------------
S=input("enter the numbers by commas" )
print(S.split(','))
print(tuple(S.split(',')))
#------------------------------------------------
A="abc.java"
A[A.index('.')+1:]
color=["blue","yellow","red","white"]
fcolor=color[0]
lcolor=color[-1]
color=["blue","yellow","red","white"]
for value in range(0,4,3):
    print (color[value])
    
for value in range(0,-2,-1):
    print (color[value])
