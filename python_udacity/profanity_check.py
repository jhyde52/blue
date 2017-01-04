import urllib

def read_text():
	youtube = open("/Users/jessicahyde/Documents/Python/python_class/youtube.txt")
	contents_of_file = youtube.read()
#	print(contents_of_file)
	youtube.close()
	profanity_check(contents_of_file)

def profanity_check(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
	output = connection.read()
	print(output)
	connection.close()
	if "true" in output:
		print ("Profanity Alert!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("The program could not scan the document properly.")

read_text()

# can't use this because contents_of_file is not a global variable
# if __name__=="__main__":
#	read_text()
#	profanity_check(contents_of_file)




###I saved a page of comments on a youtube video into a text file
###https://www.youtube.com/watch?v=K_9tX4eHztY
###create a program -I called it profanity_check.py
###create a function read_text
#def read_text():


###python standard library has built-in functions like open to open file contents-it is always available, I don't need to import anything special
###https://docs.python.org/2/library/functions.html#open
###the open function returns an OBJECT of the file type like brad was an object/instance of the turtle class
###so youtube is an object/instance of the file and starts a function like init and creates space in memory for youtube
#	youtube = open("/Users/jessicahyde/Documents/Python/youtube.txt")
	
###referring to my file as youtube now
###python has a function read to read the contents of a file
###contents_of_file is a variable I am defining
#	contents_of_file = youtube.read()
	
###
#	print(contents_of_file)
### I have to use a python function close whenever I use open
#	youtube.close()

####I need to call the function check_profanity after reading the text on my computer
###I have to pass in the contents of the file I read
#check_profanity(contents_of_file


### define a function profanity_check which takes one argument -the text I want to check
#	def profanity_check(text_to_check):

### there is a python module urllib in the python standard library that can read from the internet if we import it
###and it has a function called urlopen which takes in a link from a website
###I named the variable connection because I am opening a connection to the internet
###The urlopen returns a file that is like an object of a class
#	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)

###I will name the variable for the output/response I get from the website output and use the builtin function read
###I have to close the connection
#	output = connection.read()
#	print(output)
#	connection.close()


#read_text()