def getName():
    nameA= input ("\nWhat is your name?\n> ")
    return nameA

def getAge():
    ageA= input ("\nHow old are you?\n> ")
    return ageA

def getAddress():
    addressA= input ("\nWhere do you live?\n> ")
    return addressA

def display (nameA, ageA, addressA):
    print (f"Hi, my name is {nameA}. I am {ageA} years old and I live in {addressA}.")

name= getName()
age=getAge()
address=getAddress()

display(name, age, address)