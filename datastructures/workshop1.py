#makerlab workshop
#https://github.com/makerlabworkshop/python-2022-2023
#Python Data Structures 
#Exercice: write a program that check if a date given by a user is valid or not
#Complete the code below to solve the main problem given 
date="1800/02/23"
year =int(date[0:4])
month= int(date[5:7])
day = int(date[8:10])

if year>1900 and year <2020:
    if(month >0 and month <13 ):
        print("Month is correct.")
    print("Year correct ")
else:
    print("Year is not correct")
