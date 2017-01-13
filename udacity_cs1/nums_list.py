# A procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding biggest number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that is greater than the number y. 
# Then add this number z to the normal list and continue.


#int turns a string's element into a number
#map(function_to_apply, list_of_inputs)

def numbers_in_lists(string):
	y = -5
	sublist = []
	result = []
	for x in map(int, string):
		if x <= y:
			sublist.append(x)
		else:
			if sublist:
				result.append(sublist)
				sublist=[]
			result.append(x)
			y=x
	if sublist:
		result.append(sublist)
	print result
	return result      

numbers_in_lists('123456789')




#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result


