def printtuple(tup1):
    for day in tup1:
      print day
def createweekday():
  tup1=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
  print "printing tup1 elements"
  return tup1
def createmonts():
    tup2=("jan","feb","mar","apr","may","jun","july","aug","sep","oct","nov","dec")
    return tup2    
def concatetuple(tup1,tup2):
    tup3=tup1+tup2
    print "after concatination :",tup1
def converttuptolist(tup1):
    list1=list(tup1)
    print list1
    list1.append("holiday")
    list1.insert(4,"Movie day")
    print "list1 after append",list1