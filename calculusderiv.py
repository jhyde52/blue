
# find a derivative

def xSquared(x):
	return x**2

def getDeriv(func, x):
	h = 0.0001
	return (func(x + h) - func(x)) / h

x = 3
derivative = getDeriv(xSquared, x)
actual = 2*x

# 6.0001
print derivative

# 6
print actual


# slope definition
# slope between two points = (y2 - y1)/(x2 - x1)

# derivative definition at one point x, y
# df/dx = lim(h->0) * (f(x + h) - f(x))/h
# h is the change is x
# Interpret df as "a very tiny change in the output of f where it is understood that this tiny change is whatever results from the tiny change dx to the input.

import numpy
import matplotlib.pyplot as plt
import math

x = numpy.arange(-5, 5, 0.01)
plt.plot(x, x**2, 'b')
plt.grid(1)
plt.scatter(1.5, 1.4)

plt.show()

# epsilon is distance from chosen point (before and after the point)
epsilon = (1 * math.e) - 4
x = 1.5

# to tell python interpreter I am done, add a empty line (return)
def xSquared(x):\
	return x**2\

# to find slop of the function at a given point
# using xSquared as f, could do other functions
# 3
# A gradient is a vector that stores the partial derivatives of multivariable function.
# partial derivative (∂) is a derivative of a function of two or more variables with respect to one variable, the other(s) being treated as constant.
# In order to calculate this more complex slope, we need to isolate each variable 
# to determine how it impacts the output on its own. To do this we iterate through 
# each of the variables and calculate the derivative of the function after holding 
# all other variables constant. Each iteration produces a partial derivative which we store in the gradient.

# a gradient Always points in the direction of greatest increase of a function/ steepest ascent
# is zero at local max or local min
numericGradient =(xSquared(x + epsilon) - xSquared(x - epsilon))/(2 * epsilon)

# compare that result with symbolic derivative 2x at the test point
# 2.83
der = 2**x

# don't have to say print on terminal
numericGradient, der

