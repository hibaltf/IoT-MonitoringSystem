from objects import *
from random import *
import datetime 

# Inputs 
NamePatient= input("Name of patient: ")
AgePatient= int(input("Age "))
Sex= input("Sex: ")
blood=input("Blood :")
answer=input("is there a specific position ?: ")
if answer=='yes':
    print("Give Position :")
    print("S : Standing")
    print("U : Laying Up")
    print("D : Laying Down")
    print("R : Laying Right")
    print("L : Laying Left")
    specificPos = input()
patientCase=input("Patient Case: ")
roomNumber= input("Room Number: ")


pat1=patient(NamePatient,AgePatient,Sex,blood,patientCase,roomNumber)

