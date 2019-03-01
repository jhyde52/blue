'''--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress,
but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually,
you can do better. You scan the chemical composition of the suit's material and discover that it is formed by
extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, polymers with each other such that two adjacent
units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units'
polarity is represented by capitalization. For instance, r and R are units with the same type but opposite
polarity, whereas r and s are entirely different types and do not polymers.

For example:

In aA, a and A polymers, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible polymersions, the resulting polymer contains 10 units.

How many units remain after fully polymersing the polymer you scanned? (Note: in this puzzle and others,
the input is large; if you copy/paste your input, make sure you get the whole thing.)


PART 2:
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it
should. Your goal is to figure out which unit type is causing the most problems, remove all instances
of it (regardless of polarity), fully polymers the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully polymersing this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully polymersing this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully polymersing this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully polymersing this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type
and fully polymersing the result?

'''
# Use ord to get the Unicode symbol of the exact character and case

# Read and strip the first line
import fileinput
line = next(fileinput.input()).strip()

def reaction(line):
	result = []
	for char in line:
		if len(result) > 0 and abs(ord(char) - ord(result[-1])) == 32:
			result.pop()
        else:
        	result.append(char)
	# print result
	return len(result)

# print(reaction(line))


def polymers(input):
    # initialize list with an empty string
    result = ['']
    # for each character in the input string
    for letter in input:
        # see if the current character matches the previous when case is swapped
        if letter == result[-1].swapcase():
            # if so, pop the previous character, and don't add the current character
            result.pop()
        else:
            # otherwise, add the current character
            result.append(letter)
    # join the characters back into a single string
    return ''.join(result)

# part 1
print(len(polymers(line)))


# part 2
# find all distinct characters in the input
chars = set(line.lower())
# for each character, fully remove all instances of it (upper and lower)
# polymers the results and pick the min reaction
print(min(len(polymers(line.replace(item, '').replace(item.upper(), ''))) for item in chars))




