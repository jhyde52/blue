'''
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of
the previous message. (Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as
pressing the ENTER button)
'''

name = ""
hundred_year = 0
name = raw_input("What is your name? ")
print(name + " is a nice name.")
age = int(input("What is your age? "))
fav_num = int(input("What is your favorite number? "))
hundred_year = (2019 - age) + 100
print fav_num * (name + ", you will be 100 years old in " + str(hundred_year) + "." + "\n")
