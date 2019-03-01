'''--- Day 6: Chronal Coordinates ---

PART ONE
The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected.
Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or
dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest
distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of
integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other
coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following
list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:
--my grid would be 400 x 400?
..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance,
each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas
extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest
to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this
example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?

--- Part Two ---
On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.
In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:

Distance to coordinate A: abs(4-1) + abs(3-1) =  5
Distance to coordinate B: abs(4-1) + abs(3-6) =  6
Distance to coordinate C: abs(4-8) + abs(3-3) =  4
Distance to coordinate D: abs(4-3) + abs(3-4) =  2
Distance to coordinate E: abs(4-5) + abs(3-5) =  3
Distance to coordinate F: abs(4-8) + abs(3-9) = 10
Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
Because the total distance to all coordinates (30) is less than 32, the location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

'''


''' Attempt one (not working)
from collections import defaultdict

import numpy as np

import fileinput
line = next(fileinput.input()).strip()


def run(input):
    """don't cover a side case"""
    points = np.array([line.split(', ') for line in s.splitlines()], dtype="int16")
    x_min, y_min = np.min(points, axis=0)
    x_max, y_max = np.max(points, axis=0)
    areas = defaultdict(int)
    infinite = set()
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            curr = self.closest_point(i, j, points)
            areas[curr] += 1
            if i == x_min or i == x_max or j == y_min or j == y_max:
                infinite.add(curr)
    return max(areas[key] for key in areas if key not in infinite)

def closest_point(self, i, j, points):
    dist = np.abs(points - [i, j])
    dist = np.sum(dist, axis=1)
    ret = np.argmin(dist)
    cond = np.count_nonzero(dist[ret:] == dist[ret]) == 1
    return ret if cond else None

print run(input)
print closest_point(input) '''





# Attempt Two (works) MasterMedo

from collections import Counter

data = [map(int, i.split(', ')) for i in open('2018_06.txt').readlines()]

x_max = max(zip(*data)[0])
y_max = max(zip(*data)[1])
grid={}
for i in range(x_max):
    for j in range(y_max):
        m = min(abs(i-k)+abs(j-l) for k, l in data)
        for n, (k, l) in enumerate(data):
            if abs(i-k)+abs(j-l) == m:
                if grid.get((i, j), -1) != -1:
                    grid[i, j] = -1
                    break
                grid[i, j] = n

s = set([-1])
s = s.union(set(grid[x, y_max-1] for x in range(x_max)))
s = s.union(set(grid[x,       0] for x in range(x_max)))
s = s.union(set(grid[x_max-1, y] for y in range(y_max)))
s = s.union(set(grid[      0, y] for y in range(y_max)))

# part one
print next(i[1] for i in Counter(grid.values()).most_common() if i[0] not in s)
# part two
print sum(sum(abs(i-k)+abs(j-l) for k, l in data) < 10000 for i in range(max(zip(*data)[0]))
                                                          for j in range(max(zip(*data)[1])))