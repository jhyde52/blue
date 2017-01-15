# A procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(number):
    if number > 60:
        hours = int(number/60/60)
        if hours==1:
            time = "1 hour,"
        else:
            time = str(hours) + " hours,"
        minutes = int((number-(hours*60*60))/60)
        if minutes==1:
            time = time + " 1 minute,"
        else:
            time = time + " "+str(minutes) + " minutes,"
        
        testsec = number-(hours*60*60)-minutes*60
        if testsec % 1 == 0:
            seconds=int(testsec)
            if seconds==1:
                time = time + " 1 second"
            else:
                time = time + " "+str(seconds) + " seconds"
        else:
            seconds = round(number-(hours*60*60)-minutes*60,2)
            time = time + " "+str(seconds) + " seconds"
    else:
        hours=0
        time =str(hours) + " hours,"
        minutes = int((number-(hours*60*60))/60)
        if minutes==1:
            time = time + " 1 minute,"
        else:
            time = time + " "+str(minutes) + " minutes,"
        
        testsec = number-(hours*60*60)-minutes*60
        if testsec % 1 == 0:
            seconds=int(testsec)
            if seconds==1:
                time = time + " 1 second"
            else:
                time = time + " "+str(seconds) + " seconds"
        else:
            seconds = round(number-(hours*60*60)-minutes*60,2)
            time = time + " "+str(seconds) + " seconds"
    return time
   
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds