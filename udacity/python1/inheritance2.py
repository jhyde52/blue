class Parent():
	def __init__ (self, last_name, eye_color):
		print ("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color
#creating a new method
	def show_info (self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)

class Child(Parent):
	def __init__ (self, last_name, eye_color, number_of_toys):
		print ("Child Constructor Called")
		Parent. __init__ (self, last_name, eye_color)
		self.number_of_toys = number_of_toys
		#adding another show_info method, wrapping the number with string to display properly
	def show_info (self):
		print("Last Name - "+self.last_name)
		print("Eye Color - "+self.eye_color)
		print("Number of Toys - "+str(self.number_of_toys))		

#adding a call to the method
billy_cyrus = Parent("Cyrus", "Blue")
#billy_cyrus.show_info()
#because the child class inherits, it can also use show_info
#but if I add another method, show_info inside the Child class, the program will use that=METHOD OVERRIDING
miley_cyrus = Child ("Cyrus", "Blue", "3000")
miley_cyrus.show_info()
