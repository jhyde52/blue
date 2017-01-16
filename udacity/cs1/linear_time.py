
# which procedures scale linearly as input_list increases?

def proc1(input_list):
    maximum = None
    for element in input_list :
        if not maximum or maximum < element:
            maximum = element
    return maximum

# yes, constant time to find max element


def proc2(input_list):
    sum = 0
    while len(input_list) > 0:
        sum = sum + input_list[0]   # Assume input_list[0] is constant time
        input_list = input_list[1:]  # Assume input_list[1:] is constant time
    return sum

# yes, sum and input_list calculations are constant time

def proc3(input_list):
    for i in range(0, len(input_list)):
        for j in range(0, len(input_list)):
            if input_list[i] == input_list[j] and i != j:
                return False
    return True

# no, checking for repeated element in list, the inner loop
# could take long time if there were no repeats and it had to 
# check the whole list - this actually is going through
# len(input_list) * len(input_list) times so it is square = nonlinear