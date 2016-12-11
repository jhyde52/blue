
# go to python terminal
# time in one line at a time
# leave a blank line after the function
# call the function

import time

def time_execution(code):
	start = time.clock()
	result = eval(code)
	run_time = time.clock() - start
	return result, run_time