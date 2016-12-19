HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"

def disable():
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''

def green( msg):
    print OKGREEN + msg + ENDC

def yellow( msg):
    print WARNING + msg + ENDC

def red( msg):
    print FAIL + msg + ENDC

def blue( msg):
    print OKBLUE + msg + ENDC


def banner(msg, ch='=', length=78):
    spaced_text = ' %s ' % msg
    banner = spaced_text.center(length, ch)
    print OKGREEN + banner + ENDC