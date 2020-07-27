#!/usr/bin/env python
# coding: utf-8

#Merge two sorted list produce one sorted list ,but use only one loop while or for loop one time


str1=input("enter the first string").split(",")
num1=[]
for i in str1:
    num1.append(int(i))
str2=input("enter the second string").split(",")
num2=[]
for i in str2:
    num2.append(int(i))    
res=[]
fi=0
si=0
while fi<len(num1) and si<len(num2):
    if num1[fi]<num2[si]:
        res.append(num1[fi])
        fi+=1
    elif num1[fi]>num2[si]:
        res.append(num2[si])
        si+=1
    else:
        res.append(num1[fi])
        res.append(num2[si])
        fi+=1
        si+=1
if fi!=len(num1):
    res+=num1[fi:]
else:
    res+=num2[si:]
print(res)

#Output
#enter the first string10,20,40,60,70,80
#enter the second string5,15,25,35,45,60
#[5, 10, 15, 20, 25, 35, 40, 45, 60, 60, 70, 80]




