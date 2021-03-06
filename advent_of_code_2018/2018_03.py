"""--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who
helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately,
anomalies are still affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have
an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's
rectangle is defined as follows:

The number of inches between the left edge of the fabric and the left edge of the rectangle.
The number of inches between the top edge of the fabric and the top edge of the rectangle.
The width of the rectangle in inches.
The height of the rectangle in inches.
A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge,
2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of
fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.
For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
#1267 @ 597,458: 29x12
Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others,
does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. How many square
inches of fabric are within two or more claims?

# Notes
@ top left corner has x,y coordinate (3, 2)
And each rectangle has width and height 4x4

Use counter or default dict
Iterate over spaces the rectangle occupies
Count how many are double

[746, 884, 13, 12]
defaultdict(<type 'int'>, {})
defaultdict(<type 'int'>, {(5, 6): 1, (5, 5): 1, (6, 5): 1, (6, 6): 1}) ---counts for one square

Pass in put in terminal
python 2018-03.py 2018-03.txt
109716 """

# --- Part Two ---

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any
# other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!
# For example, in the claims above, only claim 3 is intact after all claims are made.
# What is the ID of the only claim that doesn't overlap?



import fileinput
import re
import collections

LINE_RE = re.compile(r'#\d + @(\d+),(\d+):(\d+)x(\d+)')
DIGIT_RE = re.compile(r'\d+')


def get_rectangles():
    # list_values=[]
    # for line in fileinput.input():
    #    list_values.append(map(int, DIGIT_RE.findall(line))[1:])  # put tuple in list
    #return list_values
    return[map(int, DIGIT_RE.findall(line))[1:] for line in fileinput.input()]  # list comprehension

def get_squares(rectangle):
    x_start, y_start, width, height = rectangle
    squares = []
    # range makes you a list
    for x in range (x_start, x_start + width): # loops over each square until less than reaching arg 2 (the width)
        for y in range (y_start, y_start + height):
            squares.append((x,y)) # parenthesis to tell it to create a tuple of x and y and pass it in
    return squares # a list of tuples

def overlap(rectangles):
    counts = collections.defaultdict(int)
    for re in rectangles:
        for sq in get_squares(re):
            counts[sq] += 1 # already is a tuple
            # print 'sq', sq
            # print 'counts', counts
    return counts # for each square, all have at least one

# this just gives the name of counts for inside this function to the input you defined at bottom which can be abcde
def two_or_more(counts):
    counter = 0
    list_values = counts.values()  #this is default to get list of values in dictionary
    # for value in list_values:
    #     if value >= 2: # 2 or more
    #         counter +=1
    # return counter
    return sum(value >=2 for value in list_values) # generator expression - a generator makes something you can iterate over once

def not_overlap(rectangles, counts):
    for rect in rectangles:
        squares = get_squares(rect)
        is_no_overlap = True
        for square in squares:
            if counts[square] != 1:
                is_no_overlap = False
                break
        if is_no_overlap: # if is_no_overlap = True
           return rect

rectangles = get_rectangles()
counts = overlap(rectangles) # zero argument function, need to set to variable for reuse outside function = concept called scope
print two_or_more(counts) # must pass the variable again
print not_overlap(rectangles, counts)

