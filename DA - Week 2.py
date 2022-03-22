#!/usr/bin/env python
# coding: utf-8

# # Week 2
# By: Christopher Diaz Montoya
# ID: 24707686

# ## Problem 1

# In[28]:


# Empty list created to store numbers
storedNums = [] # Loop to check over all numbers in range
for i in range (1000, 2000):
    # If multiple of 11 and not of 3 execute line below, % checks exact multiple, 
    # and not used to make sure not a multiple of 3
    if (i % 11 == 0) and not (i % 3 == 0):
        # Stores numbers that met above requirements
        storedNums.append(str(i))
# Learnt to print line from the website below to print output correctly
# https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.
# Double spacing for tabluar view of output
print(*storedNums, sep = ",  ")


# ## Problem 2

# In[29]:


# Allows user to input sentance
sentance = input("Please input a sentance to capitalise letters: ")
# Empty string to store new capitalised sentance
caps = ""
# for loop for each charecter in user inputted sentance
for i in sentance:
    # Adds it to the string Caps variable after capitalised with .capitalize()
    caps += i.capitalize()
# Printes capitalised sentance
print("Capitalised sentance is:", caps)


# ## Problem 3

# In[30]:


# Convert function created
def convert():
    # Exception handling technique used
    try:
        # Allows used to input a string number
        strInput = input("Enter a number to convert to a string: ")
        # Inputted string number now converted to int as requested
        convertedNum = int(strInput)
        # Inputted number which is now an int converted to a str again
        convertedStr = str(convertedNum)
        # Returns str as string is the desired data type output
        return convertedStr
    # If user does not enter a whole number
    except:
        # Asks user to enter a whole number
        print("Please enter in a whole number.\n")
        # Recursive call for user to try again
        return convert()

# Calls convert function and returned value assgined to results
results = convert()
# Prints user inputted str to int to str as reuqested and data type to check
print(results, type(results))


# ## Problem 4

# In[31]:


import itertools # Import from library to help iterate through all outcomes

# Below stored in list for easy access
subject = ["I", "You"]
verb = ["Read", "Borrow"]
obj = ["Shakespeare's plays","Shakespeare's poems"]

"""
Below prints and iterates over each possible out come from the lists 
mentioned with itertools while the varibles stay in the same order. 
List ensures prints in the right way
https://www.codegrepper.com/code-examples/python/how+to+find+all+combinations+of+a+list+python
"""
print(list(itertools.product(subject, verb, obj)))


# ## Problem 5.1

# In[32]:


import matplotlib.pyplot as plt # imported and given a shorter name

# Funcion to create graph
def makeGraph():
    # X and y axis gien numbers resectively
    x, y = [1,2,3], [2,4,1]
    plt.xlabel("The X axis", fontsize = 15) # Prints x label and size
    plt.ylabel("The Y axis", fontsize = 15) # Prints y label and size
    plt.title("My week 2 graph", fontsize = 20) # Prints title
    # PLots x and y values given
    plt.plot(x,y)
    # Shows graph
    plt.show()

# Calls funciton
makeGraph()


# ## Problem 5.2

# In[33]:


X = [] # Created empty lists to store values read from document
Y = []

# opens document required
nums = open(r"C:\Users\chris\Downloads\Uni\EHU year 2\Data analysis\Week 2\test.txt")
# nums is a variable which are the contents
for row in nums: # Loops all rows in the txt file
    row = row.split(" ") # splits numbers in file when it reads a space
    X.append(row[0]) # First number in index 0 is added to X 
    # int() usd to ensure graph displays in order of numbers
    Y.append(int(row[1])) # Second number is added to Y

plt.xlabel("X axis", fontsize = 15) # Prints x label
plt.ylabel("Y axis", fontsize = 15) # Prints y label
plt.title("My week 2 txt graph", fontsize = 20) # Prints title

plt.plot(X, Y) # This plots the points on the graph
plt.show() # This shows the graph


# ## Problem 6

# In[34]:


import re # Needed to check in a range of 

# Asks user for username to give the real experience but not relavant
notRelevant = input("Please enter your username: ")
# Inputted passwrd stored into variable
inpPasswords = input("Thank you, now please enter your sequence of comma seperated passwords: ")
# Password split with.split on comma
words = inpPasswords.split(",")

# Function created for checker
def checker():
    # Couunter for index 
    i = 0
    # For loop to check over each password in words
    for x in words:
        # If length of password is less than 6 characters execute below
        if len(words[i]) < 6:
            # Prints why the pass has an error
            print("Password too short, please try again.")
        # Else if length of password is more than 12 characters execute below
        elif len(words[i]) > 12:
            # Prints why the pass has an error
            print("Password too long, please try again.")
        # Else if no lower case execute below
        elif not re.search("[a-z]", x):
            print("Missing lower case, please try again.")
        # Else if no upper case execute below
        elif not re.search("[A-Z]", x):
            print("Missing upper case, please try again.")
        # Else if no numbers execute below
        elif not re.search("[0-9]", x):
            print("Missing number, please try again.")
        # Else if no special charecters execute below
        elif not re.search("[!@$\"\%^&?.,()]", x):
            print("Missing special charecter, please try again.")
        else:
            # Prints password correct
            print("Valid password. Loading...")
        # Increments by 1 end of each loop to move onto next indexed string
        i += 1

# Calls funciton
checker()

# Copy and paste below into password to check and save time or use youre own
# hi,christophe,CHRISOPHE,12s45Sf891,Ss9^$"%&$"$,hi,kahbfgilsiulhniathanon,chrisH56jd!


# ## Challenge

# In[35]:


import random # Random library

options = ["rock", "paper", "scissors"] 
computer =  random.choice(options) # Random choice form list vraible
# User input for game
choice = input("To play please enter rock, paper, or scissors in lower case: ")
# Prints to show user computers choice
print("Computer chose: ", computer)

# Gane function
def game():
    # If the same execute below
    if choice == computer:
        # Prints draw with both choices
        print("It's a draw! You chose", choice, "the computer chose", computer)
    
    # If user chooses rock
    elif choice == "rock":
        # If user chooses rock AND somputer chooses paper
        if computer == "paper":
            # Prints outcome of both choices
            print("You lost.", "Paper beats rock.")
        # If computer chooses scissors
        else:
            print("You won!", "Rock beats scissors.")
        
    # If user chooses paper
    elif choice == "paper":
        # Nested conitional stataments used for only when user makes a specifif choice
        if computer == "scissors":
            print("You lost.", "Scissors beats paper.")
        else:
            print("You won!", "Paper beats rock.")
    
    # If user chose scissors
    elif choice == "scissors":
        # If computer chose rock
        if computer == "rock":
            print("You lost.", "Rock beats Scissors.")
        # If computer chose paper
        else:
            print("You won!", "Scissors beats paper.")

    # If the user misspelt
    else:
        print("Did you spell something wrong? Try again.")
 
# Function Call
game()

