tup1=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print "printing tup1 elements"
for day in tup1:
    print day
tup2=("jan","feb","mar","apr","may","jun","july","aug","sep","oct","nov","dec")    
tup1=tup1+tup2
print "after concatination :",tup1
#del tup1[2]
list1=list(tup1)
print list1
list1.append("holiday")
list1.insert(4,"Movie day")
print "list1 after append",list1
