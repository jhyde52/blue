# Open a webpage at set intervals for a set number of times

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(360)
    webbrowser.open("https://www.youtube.com/watch?v=bjSpO2B6G4s")
    break_count = break_count + 1
