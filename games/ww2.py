from random import randint
import random
import printColor
import json
import collections

reaction_pos = ['Awesome!', 'Nice!', 'Cool!', 'Sweet!', 'Great!', 'Rad!', ':)', 'Fabulous!'] # localize later
reaction_neg = ['Bummer!', 'Shoot!', 'Oh no!', 'This is terrible!', 'Lame.', ':(', 'Dang it','You are a fat turd!'] # localize later
multi_choice = ["A","B","C","D","E","F"]
your_country = {"a":"USA","b":"France","c":"Germany","d":"Japan","e":"Italy","f":"Great Britain"}
questions = [{"a":"An eagle, fast and clever", "b":"A peacock, elegant and pretty", "c":"A lion, big and bold", "d":"A pig, rude and sloppy", "e":"A horse, hungry and strong", "f":"A bunny, long-eared and gentle.","question": "What's your spirit animal?"}, {"a":"Yeah, I dominate!","b":"Never","c":"It depends","d":"Yes","e":"Not really","f":"You're basically afraid of your own shadow.","question": "Are you scary?"}, {"a":"Swimming","b":"Track and Field","c":"Cross Country","d":"Archery","e":"Chariot Racing","f":"Iceskating","question":"Which Olympic sport would you win?"},{"a":"Water Fall","b":"Tsunami","c":"Fire","d":"Tornado","e":"Ocean Water","f":"Deadly diseases","question":"Oh no! We're being attached! What dangerous element of nature do you want to throw at your enemy?"},{"a":"Talk it out","b":"Slap them in the face","c":"Cry","d":"Declare war!","e":"Ignore it","f":"Kidnap their parents","question":"When someone says something mean about your friend, what do you do?"},{"a":"Soccer","b":"Books","c":"Barbies","d":"Dad's gun","e":"Cook Book","f":"Harry Potter books","question":"What is your favorite toy?"},{"a":"Wifi","b":"Black Clothes","c":"Nutcracker","d":"POWER","e":"Pasta","f":"Money","question":"What's at the top of your Christmas list?"},{"a":"Bad breath","b":"Bugs","c":"Homeless people","d":"Horror films","e":"Mexican food","f":"Freedom","question":"What freaks you out the most?"}]


printColor.banner("BLUE", "*", "Welcome to WW2! Take quizzes, find cool facts, make friends, and more!")

printColor.custom("TURQUOISE","It is June 1, 1937. The beautiful Golden Gate Bridge just opened and Amelia Earhart has just taken off to fly around the world!"+"\n"+ "Take the quiz to find out which country you are!")

printColor.banner("BLUE", "=", "QUIZ: Which Country Are You?")


with open('countries_data.json', 'r') as jf:
    countries = json.load(jf)

def ask_question():
	asked=[]
	i=0
	user_choices=[]
	while i < len(questions):
		if questions[i] not in asked:
			printColor.custom("TURQUOISE",questions[i]['question'])
			asked.append(questions[i]['question'])
			print " "
			print "A:", questions[i]["a"]
			print "B:", questions[i]["b"]
			print "C:", questions[i]["c"]
			print "D:", questions[i]["d"]
			print "E:", questions[i]["e"]
			print "F:", questions[i]["f"]
			print " "
			user_input = raw_input("Enter your choice: ")
			i += 1
			user_choices.append((validity(user_input,multi_choice)))
	printColor.custom("TURQUOISE", "You are done!")
	counts=collections.Counter(user_choices)
	new_list = sorted(user_choices, key = counts.get, reverse=True)
	user_country=your_country.get(new_list[0])
	print "Your country is %s!" % user_country


def validity(keyword,valid_options):
	while True:
		if keyword.capitalize() in valid_options:
			printColor.custom("BOLD", random.choice(reaction_pos))
			user_input=keyword
			return user_input
			break
		else:
			print "Invalid option."
			keyword = raw_input('Please try again: ')
			user_input=keyword

ask_question()
		#option1 + '\n' + option2 + '\n' + option3 + '\n' + option4 + '\n' + option5 + '\n' + option6) 

# answer = raw_input("I choose :")
# if answer 

# question: "What's your spirit animal?: ", options: ["A lion, big and bold", "Peacock elegant and pretty","pig rude and sloppy","horse "]



'''
	validity(user_country, countries)
	user_toy1 = raw_input("Tell me %s, what is your favorite toy?: "% user_country) # use leader later
	print random.choice(reaction_pos)
	user_fear1 = raw_input("What is your worst fear?: ")
	print random.choice(reaction_pos)
	user_wish1 = raw_input("If you could have anything you wanted, what would you wish for?: ") 
	countries[user_country]['toys'][1] = user_toy1
	countries[user_country]['fears'][1] = user_fear1
	countries[user_country]['wishes'][1] = user_wish1
	print countries[user_country]

get_inputs()

	
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



printColor.custom('RED',"WW2")
printColor.custom('ORANGE',"France")
printColor.custom('MUSTARD',"sldfas SDFS")
printColor.custom('YELLOW',"Italy")
printColor.custom('GREEN',"Germany")
printColor.custom('GREEN2',"green 2!")
printColor.custom('TURQUOISE',"Great Britain")
printColor.custom('BLUE',"USA")
printColor.custom('BLUE2',"USA")
printColor.custom('MAGENTA',"Japan")
printColor.custom('PINK',"pink")
printColor.custom('WHITE',"white!")
printColor.custom('BOLD',"bold!")

'''