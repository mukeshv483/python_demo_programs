import calendar;

print calendar.calendar(2016,w=2,l=1,c=10)
print "leap days between the years 1980 to 2025 are:",calendar.leapdays(1980,2025)
year=input("enter year to check leap year")
if type(year)!=int:
    print "wrong input type please enter a integer value"
    year=input("enter year to check leap year")
if calendar.isleap(year)==True:
    print "given year is a leap year"
else:
    print "given year is not a leap year"
