'''
Exercise 2 (and Solution)
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''


fav_num = 0
fav_num = int(input("What is your favorite number? "))

def check_even(fav_num):
	if fav_num % 2 == 0:
		if fav_num % 4 == 0:
			print("Your favorite number is even and divisible by four!")
		else:
			print("Your favorite number is even!")
	else:
		print("Your favorite number is odd!")

num = int(input("What is your lucky number? "))
check = int(input("What is your unlucky number? "))

def check_divisible(num, check):
	if num % check == 0:
		print("Your lucky number is divisible by your unlucky number!")
	else:
		print("Your lucky number is not divisible by your unlucky number!")


check_even(fav_num)
check_divisible(num, check)