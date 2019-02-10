#Conversion from number to string

a=input("Input some number:")
print("Now "+a+" is a Number.")
str(a)
print("After str(), "+a+" is a String")

#Conversion from string to number

b=input("\nInput some string:")
print("Now "+b+" is a String")
int(b)
print("After int(), "+b+" is a Number")

#Conversion from string to list

c=input("\nInput some string:")
print('Now "'+c+'" is a String.')
list=list(c)
print('After list=c.split(), the following elements are of a list.\n',list)

#Conversion from list to string

print('\nNow "',list,'" is a List.')
str=""
str=str.join(list)
print('After str=c.join(list), the following is generated string.\n',str)
