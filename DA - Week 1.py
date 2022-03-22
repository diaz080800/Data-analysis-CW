#!/usr/bin/env python
# coding: utf-8

# # Week 1
# By: Christopher Diaz Montoya
# ID: 24707686

# ## Problem 1

# In[1]:


# Here I used varibles to store the values, then added both variables.
num1 = 52 
num2 = 78

# num1 + num2 is in brackets so this is figured out first before printing.
# "," was learnt last academic year in uni to display it on 1 line.
print("The result is:", (num1 + num2))


# ## Problem 2

# In[2]:


""" 
Here I used a for loop which repeats for the amount of times 
as there are numbers between the range of numbers 0 - 4, this means
it loops over 4 times and executes the print function for each of the 
4 times, thus printing out hello, world 4 itmes.
"""

for x in range(0,4):
    print("Hello, World!")


# ## Problem 3

# In[3]:


"""
Here I used \ for a new line in the string (code), \n for a new line in
the output and \t for tabs, this creates 4 spaces in the output. All learnt
last academic year along with being recapping during last semesters lectures.
"""

print("Twinkle, twinkle, little star, \n\tHow I wonder what you are!\n\t\tUp above the world so high, \n \n\t\tLike a diamond in the sky.\nTwinkle twinkle, little star, \n\tHow I wonder what you are.")


# ## Problem 4

# In[4]:


import random # Imported library to help chose a random library
# Imports library to help choose random charecters as it is easier than given code help
import string

# Code given to input a number the length of the password
def userInput():
    # Exception handling code used to only allow users to input whole numbers
    try:
        # Converts user password length to integer assigned to variable
        passLen = int(input("Enter the desired random password length that is 4 charecters or greater.        \nOr the password will automatically be 8 charecters long for strenghtened security:"))
        # If password bigger or equal to 4
        if passLen >= 4:
            # Returns user passsword length
            return passLen
        # If smaller than 4
        else:
            # Makes password automatically 8 charecters long for password security
            passLen = 8
            # Returns password length which is 8
            return passLen
            
    # If a non whole number entered below is executed
    except:
        # Asks user to enter a whole number
        print("Please enter in a whole number larger than 4.\n")
        # Recursive call for function
        return userInput()

# User desired password length 
passLength = userInput()

# Here charChoice variable allows for a letter, didigt or punctuation to be added later
charChoice = string.ascii_letters + string.digits + string.punctuation

# Variable created to store random password
passwrd = random.choice(string.ascii_lowercase)
# Each line += used to add charecters to randomly generated password
passwrd += random.choice(string.ascii_uppercase)
# Random.choice() used to generate a random choice of what is in the brackets
passwrd += random.choice(string.digits)
# String.choice was used to import a random choice from the string library
passwrd += random.choice(string.punctuation)

# For loop that goes up to length of the password, minus 4 as the 4 
# needed elements in the password were already added to the passwrd variable.
print(passLength)
for i in range (passLength - 4):
    # A random choice form the charChoice variable was added to the password
    # varibale each loop.
    passwrd += random.choice(charChoice)

# Password turned into a list and assigned to a new varibale for shuffling
# as would not work with string
passwrdList = list(passwrd)

# Random shuffle on the passwrd list
random.SystemRandom().shuffle(passwrdList)

# List added to a new empty string variable so it prints with no brackets or commas,
# as a list would. Vairable named password is an empty string as used "".join()
password = "".join(passwrdList)

# Prints the generated password
print("The generated password:", password)


# ## Challenge Problem

# In[10]:


# Allows user to give input with input() funciton
word = input("Enter a sentance or phrase to generate the acronym: ")
# Splits the sentance in the spaces and assigns to varible wordList
wordList = word.split(" ")
# x is a counter for the user to know the acronym is on
x = 1

# For loop for all the words in the wordList
for word in wordList:
    # Prints the first letter of each word each loop
    # Done by using indexing each word in the word list with [0], indexing count starts from 0
    # hence first letter of each word (as each is looped over) is printed for acronym
    print("First letter in word", (x), ":", word[0])
    # Counter increases by 1 each time with += to let user know which words first letter
    # was printed
    x += 1

