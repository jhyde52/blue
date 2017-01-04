import time
import webbrowser

print "This program will tell you when it is time to go!"

run_once = 0
while 1:
    if run_once == 0:
        time.ctime() == "Wed Mar 16 01:55:00 2016"
        print "Let's go!"
        webbrowser.open("http://ccare.stanford.edu/events/perspectives-on-compassion-new-thinking-from-stanford-university-and-the-university-of-edinburgh/")
        run_once = 1

