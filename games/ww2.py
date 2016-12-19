import random
import printColor
import json

reaction_pos = ['Awesome!', 'Nice!', 'Cool!', 'Sweet!', 'Great!', 'Rad!', ':)'] # localize later
reaction_neg = ['Bummer!', 'Shoot!', 'Oh no!', 'This is terrible!', 'Lame.', ':('] # localize later

printColor.banner("WW2")
print("It is June 1, 1937. The beautiful Golden Gate Bridge just opened and Amelia Earhart has just taken off to fly around the world! Which country do you want to be?")

printColor.red("France")
printColor.green ("Italy")
printColor.blue("USA")
printColor.red("Japan")
printColor.green("Germany")
printColor.blue("Great Britain")

user_country = raw_input('Enter a country: ').capitalize()

while True:
	if user_country.capitalize() in countries:
		print random.choice(reaction_pos)
		user_toy= raw_input("Tell me %s, what is your favorite toy?: "% user_country) # use leader later
		print random.choice(reaction_pos)
		break
	else: 
		print "Invalid option. Please try again."
		user_country = raw_input('Enter a country: ')
		continue


#functions = lose_toy, realize_fear,lose_friend, leader_dies, lose_wish
# if empty list, print none
# add greeting, facts

penalties = ["all women die", "all men die", "all animals die", "all plants die"]


