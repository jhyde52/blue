import random
import printColor
import json

reaction_pos = ['Awesome!', 'Nice!', 'Cool!', 'Sweet!', 'Great!', 'Rad!', ':)'] # localize later
reaction_neg = ['Bummer!', 'Shoot!', 'Oh no!', 'This is terrible!', 'Lame.', ':('] # localize later

printColor.banner("WW2","MAGENTA", "+")
print("It is June 1, 1937. The beautiful Golden Gate Bridge just opened and Amelia Earhart has just taken off to fly around the world! Which country do you want to be?")

printColor.custom("RED","France")
printColor.custom("GREEN","Italy")
printColor.custom("YELLOW","USA")
printColor.custom("ORANGE","Japan")
printColor.custom("BLUE","Germany")
printColor.custom("MAGENTA","Great Britain")

with open('countries_data.json', 'r') as jf:
    countries = json.load(jf)

def validity(keyword,valid_options):
	while True:
		if keyword.capitalize() in valid_options:
			print random.choice(reaction_pos)
			break
		else:
			print "Invalid option."
			user_country = raw_input('Please try again: ')
			continue

def get_inputs():
	user_country = (raw_input('Enter a country: ')).capitalize()
	validity(user_country, countries)
	user_toy1 = raw_input("Tell me %s, what is your favorite toy?: "% user_country) # use leader later
	print random.choice(reaction_pos)
	user_fear1 = raw_input("What is your worst fear?: ")
	print random.choice(reaction_pos)
	user_wish1 = raw_input("If you could have anything you wanted, what would you wish for?: ") 
	countries[user_country]['toys'][1] = user_toy1
	countries[user_country]['fears'][1] = user_fear1
	countries[user_country]['wishes'][1] = user_wish1
	print random.choice(reaction_pos)
	#print countries[user_country]

get_inputs()

'''	
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
penalties = ["all women die", "all men die", "all animals die", "all plants die"]
# if empty list, print none
'''

