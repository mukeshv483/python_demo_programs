import time;	
import calendar;
localtime1 = time.localtime(time.time())
print localtime1
cur_month=localtime1[1]
cur_year=localtime1[0]
print "current month is:",cur_month
print "current year is:",cur_year
localtime = time.asctime( time.localtime(time.time()) )
print "current localtime time is :",localtime
print "current month's calendar is:"
cal = calendar.month(cur_year,cur_month)
print cal 
