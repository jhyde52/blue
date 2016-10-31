# Goal to find how many days between two dates (valid dates going forward)
# Input=2 dates, Output=return number of days
# Look at examples to see relationships
# Look at solving this systematically like the steps a human would take
# but humans are lazier than computers so computer maybe has a simpler, easier, mechanical way
# How to validly encode the inputs?-in this case already see 6 inputs
# To be defensive programmers we should do some checks that the inputs are valid
# Find number of days in the start month
# Take start day, subtract it from the days in start month
# For partial years, find which months in the span and multiple by month_days times, add the days
# Add any remaining days that happen after 


def daysinmonth(year,month):
   if month in (1,3,5,7,8,10,12):
      return 31
   else:
      if month ==2:
         if isleapyear(year):
            return 29
         return 28
      else: 
         return 30
   return 30



def nextday(year,month,day):
   if day < daysinmonth(year,month):
      return year, month, day + 1
   else:
      if month < 12:
         return year, month+1, 1
      else:
         return year+1, 1, 1 

def dateisbefore(year1, month1, day1, year2, month2, day2):
   if year1<year2:
      return True
   if year1==year2:
      if month1<month2:
         return True
      if month1==month2:
         return day1<day2
   return False  

def daysbetweendates(year1, month1, day1, year2, month2, day2):
   assert not dateisbefore(year2,month2,day2,year1,month1,day1)
   days=0
   while dateisbefore(year1, month1, day1, year2, month2, day2):
      year1,month1,day1=nextday(year1,month1,day1)
      days+=1   
   return days
    
def isleapyear(year):
   if year % 400 ==0:
      return True
   if year % 100==0:
      return False
   if year % 4==0:
      return True
   return False

def test():
   test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
   for (args, answer) in test_cases:
      result = daysbetweendates(*args)
      if result != answer:
         print "Test with data:", args, "failed"
      else:
         print "Test case passed!"

test()


# Inputs
# Outputs
# Work through examples by hand
# Simple mechanical solution
# Develop incrementally and test as we go