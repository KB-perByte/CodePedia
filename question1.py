#!/usr/bin/python

'''
BEGINNER
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name
'''
name = str(raw_input("Enter your Username: "))
strData = 'Hello <<UserName>>, How are you?'
if len(name) >= 3 : #and name.isalnum():
    strData = strData.replace('<<UserName>>', name[:-1])
    print strData
else:
    print("Use a valid username")

