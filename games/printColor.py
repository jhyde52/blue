# custom colors!


colors = {'RED' : '\033[31m','ORANGE' : '\033[91m','MUSTARD' : '\033[33m','YELLOW' : '\033[93m','GREEN' : '\033[92m','GREEN2' : '\033[32m','TURQUOISE' : '\033[36m','BLUE' : '\033[94m','BLUE2' : '\033[34m','MAGENTA' : '\033[35m','PINK' : '\033[95m','WHITE' :'\033[37m', 'ENDC':'\033[0m', 'BOLD': '\033[1m'}



def custom(color, msg):
    print colors[color] + str(msg) + colors['ENDC'] 

def banner(color, ch, msg, length=88):
    spaced_text = ' %s ' % msg
    banner = spaced_text.center(length, ch)
    print colors[color] + banner + colors['ENDC']


# print banner("hi", 'GREEN')
# print custom('RED','hi')
# print custom('ORANGE','hi orange')

