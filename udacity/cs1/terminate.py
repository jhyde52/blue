# For each of the procedures defined below, check the box if the procedure always terminates for all inputs that are natural numbers (1,2,3...).

def proc1(n):
   while True:
      n = n - 1
      if n == 0:
         break
   return 3

# yes, has a break and will reach 0


def proc2(n):
   if n == 0:
      return n
   return 1 + proc2(n - 2)

# no, if you start with an odd number you skip zero


def proc3(n):
   if n <= 3:
      return 1
   return proc3(n - 1) + proc3(n - 2) + proc3(n - 3)

# yes, we do get smaller than 3