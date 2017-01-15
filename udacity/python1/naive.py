#algorithm case study

def naive(a,b):
	x = a; y = b
	z= 0
	while x > 0:
		z = z + y
		x = x - 1
	return z

print naive(4,8)



ab=xy+z

#before while loop
x=a; y=b
z=0

therefore 

ab=xy+z
ab = a*b+0


#after while loop
xp=x-1
yp=y
zp=z+y

ab=(x-1)(y)+(z+y)
ab=xy-y+z+y
ab=xy+z





#python
#to write python
#write a file in sublime
#save it with the extension .py
#then in terminal, navigate to that folder and use the command python to run it
#python naive.py


#russian peasant/ancient egyptian algorithm

def russian(a,b):
	x = a; y = b
	while x > 0:
		if x % 2 == 1: z = z + y
		y = y << 1
		x = x >> 1
	return z

print russian(2,5)

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





