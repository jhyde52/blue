# Author: Jessica

""" Day One Requirements:
The device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the
current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a
frequency of zero, the following changes would occur:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6
Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency
have been applied?

430

BEGINNER VERSION
"""


def main():
    freq = []   # create empty list
    for i in open("2018-01.txt", 'r'):  # open file
        freq.append(i)  # add values from file to the list

    part_1(freq) # pass list to functions below
    part_2(freq)

def part_1(freq):
    sum = 0
    for line in freq:
        sum += int(line)  # cast as int
    print(sum)

def part_2(freq):
    sum = 0 # start sum at zero
    dict_f = {0:True}  # dictionary
    dup = False
    while True:
        for line in freq:
            sum += int(line)
            if sum in dict_f:
                dup = True
                print(sum)
                break
            else:  #  store value in dictionary
                dict_f[sum] = True
        if dup:
            break

if __name__ == "__main__":
    main()


"""Part Two:
You notice that the device repeats the same frequency change list over and over. To calibrate the device,
you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2. Note that your device might need to repeat its
list of frequency changes many times before a duplicate frequency is found, and that duplicates might
be found while in the middle of processing the list.

Here are other examples:

+1, -1 first reaches 0 twice.
+3, +3, +4, -2, -4 first reaches 10 twice.
-6, +3, +8, +5, -6 first reaches 5 twice.
+7, +7, -2, -7, -4 first reaches 14 twice.
What is the first frequency your device reaches twice?

462
"""


""" ADVANCED VERSION
map takes first argument as a function, second as a iterable
https://docs.python.org/3/library/functions.html#map

python aoc.py 1.txt
or
type python.py and then copy in data in cmd line

part 2
itertools
https://docs.python.org/2/library/itertools.html

set has nicer syntax and can do union or intersect
and don't have to worry about setting to true
"""

import fileinput
print(sum(map(int,fileinput.input())))

seen = () # or seen {0} to safer for corner cases
freq = 0
for adjust in itertools.cycle(numbers):
    freq += numbers
    if freq in seen:
        print(freq)
        break
    seen.add(freq)