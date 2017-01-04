
#russian peasant/ancient egyptian algorithm

def russian(a,b):
	x = a; y = b
	z = 0
	while x > 0:
		if x % 2 == 1: z = z + y
		y = y << 1
		x = x >> 1
	return z

print russian(20,7)

#modulo operator
#if x % 2 == 1
#(this checks if x is divided by 2, is the remainder 1)
#(this is saying if x is odd)
#whenever x is odd it adds y to z and then no matter what it doubles y, halves x and 
#goes back to the loop until x is 0.


#bit shift
#17>>1
#10001
#shifts over 1
#to 1000
#so it roughly halves the number but if it is odd it rounds down


#x 2, 1, 0
#y 5, 10, 20
#z 0, 10, 10

#   base case is true
#   ab=xy+z

#if x is even
#if x is odd

#(20,7,0)        0
#10, 14, 0       0
#5, 28, 0         
#2, 56, 28**
#1, 112, 28
#0, 224, 140***

#there were two additions of x and y which is the same as 
#each time there is an odd number in the first sequence, an addition takes place
#001010  this is binary representation for 20







