#A program for fetching email, contact, PAN from a string using regular expresion
#Demo input string: Hello! my email id is pratik149@yahoo.com , my contact number is 9854785412 and my pan number is danop21oa

import re

def userdetails(): #A function of regular expression for id, contact and PAN

        #For removing puntuations
        str = input("Tell me your email id, contact number and PAN no. :")
        str1=(re.sub("[!#,()'*]"," ",str)) #regex for substituing puntuations
        print(str1)

        #Fethcing email id
        id=(re.findall("\S+[@]\S+",str1))  #regex for email id
        print(id)

        #Fetching contact number
        contact = (re.findall("(\d+)", str1))  #regex for contact
        for i in range(0,len(contact)):
            n=len(contact[i])
            if (n>=8 and n<=10):
                no=[int(''.join(list(contact[i])))]
                print(no)

        #Fecthing pan number
        pan=(re.findall("\D{5}\d{2}\D{2}",str1)) #regex for PAN number
        print(pan)

        main()

def main():
    decision=input("Do you want to enter user details? Enter Y or N: ")

    if(decision=='Y' or decision=='y'):
            userdetails()
    elif(decision=='N' or decision=='n'):
        print("Program ended.")
        exit()
    else:
        print("Incorrect Input")
        main()

main()


