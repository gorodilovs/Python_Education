import os
import re
from contactStruct import name_data, surname_data, phone_data, adress_data

fileName = "book.txt"

def readBook():
    if os.path.exists(fileName):
        print("Telephone book:")
        with open(fileName, "r") as contacts:
            listOfContacts = contacts.readlines()
            for lineContact in listOfContacts:
                print(lineContact)
    else:
        print("File is missing!")

def writeBook():
    print("Input contact:")
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    with open(fileName, 'a') as contacts:
        contacts.write(f"{name}; {surname}; {phone}; {adress}\n")

def searchBook():
    toFind = input("Input string to find: ")

    with open(fileName, "r") as contacts:
        listOfContacts = contacts.readlines()
        if ";" in toFind:
            toFindElements = toFind.split(";")
        else:
            toFindElements = [toFind]
        isFound = False

        for lineContact in listOfContacts:
            elementContactList = lineContact.split("; ")
            count = 0

            for elementContact in elementContactList:                
                for toFindOneElement in toFindElements:                 
                    if toFindOneElement.lower() in elementContact.lower() and (len(toFindOneElement.lower()) == len(elementContact.lower())):
                        count += 1
            if count == len(toFindElements):
                print(lineContact)
                isFound = True
        
        if not isFound:
            print("Value is missing!")



def editBook():
    toFind = input("Input string to find: ")

    with open(fileName, "r+") as contacts:
        listOfContacts = contacts.readlines()
        if ";" in toFind:
            toFindElements = toFind.split("; ")
        else:
            toFindElements = [toFind]
        isFound = False
        lineCounter = 0

        for lineContact in listOfContacts:
            elementContactList = lineContact.split("; ")
            countWords = 0
            lineCounter += 1
            
            for elementContact in elementContactList:                
                for toFindOneElement in toFindElements:                 
                    if toFindOneElement.lower() in elementContact.lower() and (len(toFindOneElement.lower()) == len(elementContact.lower())):
                        countWords += 1
            if countWords == len(toFindElements):
                print(lineCounter, lineContact)
                isFound = True
        
        if not isFound:
            print("Value is missing!")

        if isFound:
            stringToReplace = int(input("Input number of matched Contact to replace: "))


    with open(fileName, "w") as contacts:
        listToWrite = ""
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        adress = adress_data()
        listOfContacts[stringToReplace-1] = (f"{name}; {surname}; {phone}; {adress}\n")
        
        for i in range(len(listOfContacts)):
            listToWrite += (f"{listOfContacts[i]}")
        
        contacts.writelines(listToWrite)

def deleteBook():
    toFind = input("Input string to find: ")

    with open(fileName, "r+") as contacts:
        listOfContacts = contacts.readlines()
        if ";" in toFind:
            toFindElements = toFind.split("; ")
        else:
            toFindElements = [toFind]
        isFound = False
        lineCounter = 0

        for lineContact in listOfContacts:
            elementContactList = lineContact.split("; ")
            countWords = 0
            lineCounter += 1
            
            for elementContact in elementContactList:                
                for toFindOneElement in toFindElements:                 
                    if toFindOneElement.lower() in elementContact.lower() and (len(toFindOneElement.lower()) == len(elementContact.lower())):
                        countWords += 1
            if countWords == len(toFindElements):
                print(lineCounter, lineContact)
                isFound = True
        
        if not isFound:
            print("Value is missing!")

        if isFound:
            stringToReplace = int(input("Input number of matched Contact to delete: "))

        with open(fileName, "w") as contacts:
            listToWrite = ""
            listOfContacts[stringToReplace-1] = ""
            
            for i in range(len(listOfContacts)):
                listToWrite += (f"{listOfContacts[i]}")
            
            contacts.writelines(listToWrite)
