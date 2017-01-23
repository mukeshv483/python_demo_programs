def printlist(empin):  
     for name in empin:
         print "emp info is :",name

def printindex(empname):
    index=input("Enter index to print name")
    print "emp name at given index is: ",empname[index]
def printindexid(empid):
    index=input("Enter index to print")
    print "emp id at given index is: ",empid[index]
def empinfo(empname,empid):
    for i in range(0,10):
        print "empname and emp id is ",empname[i],empid[i]
def splitlist(empname):
    print empname[4:9]
    print empname[3:]
def listrepeat(empname):
    count=input("enter number to repeate the list")
    print empname*count
def listconcate(empname,empid):
    list3=empname + empid
    print list3






