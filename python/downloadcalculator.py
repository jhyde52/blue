# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

# creates a dictionary of key value pairs to show time with numbers and words
# string.format() lets you pass in a predefined dictionary of arguments instead of unpacking them 1 at a time
# lambda functions don't need a return statement
# makes sure to use plural units of time when appropriate, apply that function to the individual unit/type string functions
builder = lambda value, word : "{value} {word}".format(value=value, word=word)
time_string = lambda time, type: builder(time, type) if time == 1 else builder(time, type + "s")
hours_string = lambda h: time_string(h, "hour")
seconds_string = lambda s: time_string(s, "second")
minutes_string = lambda m: time_string(m, "minute")
hours_minutes_seconds = lambda h, m, s: "{h}, {m}, {s}".format(h=h, m=m, s=s)

# segment the total seconds into hour, minute, second units
hours = lambda t: hours_string(int(t / 3600))
minutes = lambda t: minutes_string(int((t % 3600) / 60))
seconds = lambda t : seconds_string(t % 3600 % 60)

# now pass in the time segmented into units to get the appropriate strings added on to the numbers
convert_seconds = lambda t: hours_minutes_seconds(hours(t), minutes(t), seconds(t))

# create a dictionary for converting bits and bytes and kilo/mega/giga/tera
bits = dict(k=2**10, M=2**20, G=2**30, T=2**40, b=1, B=8)

# Beautifully multiply the file size and bandwidth number by the appropriate conversions
def download_time(file_size, filesize_unit, bandwidth, bandwidth_units):
    file_bits = float(file_size) * bits[file_size_unit[0]] * bits[file_size_unit[1]]    
    bandwidth_bits = bandwidth * bits[bandwidth_units[0]] * bits[bandwidth_units[1]]
    return convert_seconds(file_bits / bandwidth_bits)




print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


