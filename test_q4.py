import csv   #imports csv library

file = open("Books.csv","a")    #opens the csv to append it
title = input("Enter a title: ")    # inputs from user as title
author = input("Enter author: ")    #inputs from user as author
year = input("Enter year released: ")   #inputs from user as year released
newrecord - title + "," + author + "," + year + "\n"  #creates a new records and combines user input, with newline
file.write(str(newrecord))  #writes the newrecord as a string
file.close()                #closes the file

file = open(Books.csv","r") #opens the csv as read only
for row in file:            # checks for each row in the record and prints to screen
    print(row)
file.close()