# -*- coding: utf-8 -*-
"""p31.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dMGLD7BctVAjwYcCiV-egOFxil4cExk6
"""

stud={}
m=int(input("Enter the number of students:"))
for i in range(0,m):
    n=input("Enter the name:")
    stud[n]=int(input("Enter mark out of 20:"))
print(stud)
lis=[]
lis+=stud.keys()
lis.sort()
for i in range(m):
    print(lis[i],"\t\t",stud[lis[i]])