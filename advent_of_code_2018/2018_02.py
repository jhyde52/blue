# Author: Jessica

""" --- Day 2: Inventory Management System ---
You stop falling through time, catch your breath, and check the screen on the device.
"Destination reached. Current Year: 1518. Current Location: North Pole Utility Closet
83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either.
But now that so many people have chimneys, maybe he could sneak in that way?" Another
voice responds, "Actually, we've been working on a new kind of suit that would let
him fit through tight spaces like that. But, I heard that a few days ago, they lost
the prototype fabric, the design plans, everything! Nobody on the team can even seem
to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd
be stored together, so the box IDs should be similar. Too bad it would take forever
to search the warehouse for two similar box IDs..." They walk too far away to hear
any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you
could cause if you were discovered - and use your fancy wrist device to quickly
scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting
the number that have an ID containing exactly two of any letter and then separately
counting those with exactly three of any letter. You can multiply those two counts
together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

abcdef contains no letters that appear exactly two or three times.
bababc contains two a and three b, so it counts for both.
abbcde contains two b, but no letter appears exactly three times.
abcccd contains three c, but no letter appears exactly two times.
aabcdd contains two a and two d, but it only counts once.
abcdee contains two e.
ababab contains three a and three b, but it only counts once.
Of these box IDs, four of them contain a letter which appears exactly twice, and three
of them contain a letter which appears exactly three times. Multiplying these together
produces a checksum of 4 * 3 = 12.

with open("2018-02.txt", "r") as input_file:
input = [line.strip() for line in input_file]

Part one: What is the checksum for your list of box IDs?
Make a dictionary and insert each letter and add a freq each time we see it in that word.
7776


--- Part Two ---
Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings.
For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However,
the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the
correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by
removing the differing character from either ID, producing fgij.)

wlkigsqyfecjqqmnxaktdrhbz
wlkiogsqyfecjqqmnxaktdrhbz
wlkiwgsqyfecjqqmnxaktdrhbz

BEGINNER VERSION
"""


def main():
	ids = []
	for line in open('2018-02.txt'):  # each word in list
		entry = line.strip()
		ids.append(entry)

	part_1(ids)
	part_2(ids)

def part_1(ids):
	count_2 = 0
	count_3 = 0
	for entry in ids:
	    count = {}
	    for letter in entry:  # each letter in the word
	        if letter not in count:
	            count[letter] = 0  # stores in dictionary letter w: count 0
	        count[letter] += 1  # if already there, stores in dict with plus one count
	    has_two = False
	    has_three = False
	    for k,v in count.items(): # list comp, each key:value pair
	    	if v==2:
	            has_two = True
	        if v==3:
	            has_three = True
	    if has_two: # totals counts up
	        count_2 += 1
	    if has_three:
	        count_3 += 1
	print count_2 * count_3

def part_2(ids):
	for entry in ids:
		for entry_2 in ids:
			diff = 0
			for letter in range(len(entry)):
				if entry[letter] != entry_2[letter]:
					diff += 1
	        if diff == 1:
	            ans = []
	            for letter in range(len(entry)):
	                if entry[letter] == entry_2[letter]:
	                    ans.append(entry[letter])
	            print ''.join(ans)
	            print entry,entry_2

if __name__ == "__main__":
	main()



"""
ADVANCED VERSION
counts = collections.defaultdict(int) is like Counter
counts['a'] += 2

on command line:
python aoc_2.py input.txt

replace for loop:
counts.update(set(letter_counts.value()))

sum true and false tells you how many are true

"""


import collections
import fileinput
import itertools

counts = collections.Counter() # this is a type of dictionary, when you initialize it defaults undefined values to 0--otherwise you would get error cuz default is null

for line in fileinput.input:
    line = line.strip()
    letter_counts = collections.Counter(line)  #counts how many times each things appears
    counts_seen = set(letter_counts.value)
    for count in counts_seen:
        counts[count]
print (counts[2] * counts[3])



# part two:
# use combinations from itertools
# zip
# https://docs.python.org/3/library/functions.html#zip
# zips [1,2,3][2,3,4]
# (1,2)(2,3)(3,4)

counts = collections.Counter()
serials = map(str.strip, fileinput.input())
for serial in serials:
    letter_counts = collections.Counter(line)
    counts.update(set(letter_counts.value))

for serial1, serial2 in itertools.combinations(serials):
    diffs = sum(
        c1 != c2
        for c1, c2 in zip(serial1, serial2))

if len(same_chars) == len(serial1):
    print(same_chars)
    break
