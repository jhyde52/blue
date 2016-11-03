# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.

# The input to the function will be an encrypted body of text that only contains the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.


# version 2

def freq_analysis(message):
	freq_list=[]
	alpha='abcdefghijklmnopqrstuvwxyz'
	n=float(len(message))
	for x in alpha:
		freq_letter=0
		if x in message:
			positionmessage = 0
			while positionmessage < len(message):
				if x == message[positionmessage]:
					freq_letter +=1
				positionmessage +=1
			freq_list.append(freq_letter)
		else:
			freq_list.append(freq_letter)	
	freq_list.append(freq_letter)
	for item in freq_list:
		freq_list[freq_list.index(item)] = item/n

	return freq_list

# index lets you find the number of that string element in the list
# for when you list is not numbers



 # beginner version
def freq_analysis(message):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	freq_list = []
	letters = 0
	while letters < len(alphabet):
		start = 0
		freqOfLetter = 0
		while start < len(message):
			if message.find(alphabet[letters],start)!= -1:
				start = message.find(alphabet[letters],start)+1
				freqOfLetter+=1
			else:
				break
		e = freqOfLetter*1./ len(message)
		freq_list.append(e)
		letters+=1
	return freq_list


# advanced version
def freq_analysis(message):
    result = []
    for letter in list('abcdefghijklmnopqrstuvwxyz'):
        result.append(message.count(letter)/float(len(message)))
    return result

# list turns a string into a list
# count counts instances of each item in the list that are in the message




#Tests

print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]









