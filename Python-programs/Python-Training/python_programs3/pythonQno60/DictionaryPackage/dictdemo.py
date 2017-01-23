import time;
import calendar;
def cmpdict(dict1,dict2,dict3):
    if cmp(dict1,dict2)==1 and cmp(dict1,dict3)==1:
        print "dict1 is biggest"
    if cmp(dict2,dict1)==1 and cmp(dict2,dict3)==1:
        print "dict2 is biggest"
    if cmp(dict3,dict1)==1 and cmp(dict3,dict2)==1:
        print "dict3 is biggest"    
    if cmp(dict1,dict2)==0 and cmp(dict1,dict3)==0:
        print "all are equal"

def dictlength(dict1):
    print "length of dict is:",len(dict1)

def dicttostr(dict1):
    print "converting dictionary into string"
    str1=str(dict1)
    print str1

def concatdict(dict1,dict2):
    str1=str(dict1)
    str2=str(dict2)
    finalstr=str1+str2
    print "final string after concatination",finalstr
 
 
def updatedict(dict1,dict2):
    dict1.update(dict2)
    print dict1

def updatevalue(dict1):
    sal=input("new value for salary")
    dict1['Salary']=sal
    print dict1
    ag=input("new value for age")
    dict1['Age']=ag
    print dict1
    grd=input("new value for grade")
    dict1['grade']="B1"
    print dict1
def printallkeyvalues(dict1):
    keys= dict1.keys()
    values= dict1.values()
    print "keys are:"
    for key in keys:
        print key
    print "values are :"
    for value in values :
     print value

def deleteattribute(dict1,key):
    keys= dict1.keys()
    if key in keys:
        del dict1[key]
    else :
        print "key not found can not delete"
    print dict1
def currenttime():
    localtime1 = time.localtime(time.time())
    print localtime1
    
def currmthcaledar():
    localtime1 = time.localtime(time.time())
    cur_month=localtime1[1]
    cur_year=localtime1[0]
    print "current month is:",cur_month
    print "current year is:",cur_year
    localtime = time.asctime( time.localtime(time.time()) )
    print "current localtime time is :",localtime
    print "current month's calendar is:"
    cal = calendar.month(cur_year,cur_month)
    print cal 

 
def printyearcal(year):
    print "calendar of %s year is" %(year)
    print calendar.calendar(year,w=2,l=1,c=10)

def isleapyear(): 
    year=input("enter year to check leap year")
    if type(year)!=int:
        print "wrong input type please enter a integer value"
        year=input("enter year to check leap year")
    if calendar.isleap(year)==True:
        print "given year is a leap year"
    else:
        print "given year is not a leap year"
