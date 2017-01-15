class Parent():
	def __init__ (self, last_name, eye_color):
		print ("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color



#by putting Parent inside, we are saying this class inherited everything from the class we called Parent
#we have to list all the variables from Parent as arguments:
#and then we want to initialize those variables of the parent and child classes
class Child(Parent):
	def __init__ (self, last_name, eye_color, number_of_toys):
		print ("Child Constructor Called")
		Parent. __init__ (self, last_name, eye_color)
		self.number_of_toys = number_of_toys


#instance of the class Parent
billy_cyrus = Parent("Cyrus", "blue")
print (billy_cyrus.last_name)
print (billy_cyrus.eye_color)

#instance of the class Child with 3 necessary arguments
#(if parent class instance is no there, this will run first and init the child class, then the parent class, 
#then it will initalize the variables for Parent, then the variable for child (number of toys) then print this last name and toys
miley_cyrus = Child ("Cyrus", "blue", "3000")
print (miley_cyrus.last_name)
print (miley_cyrus.eye_color)
print (miley_cyrus.number_of_toys)
