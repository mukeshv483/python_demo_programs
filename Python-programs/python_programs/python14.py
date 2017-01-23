empid=[1,2,3,4,5,6,7,8,9,10]
empname=["a","b","c","d","e","f","g","h","i","j"]
for name in empname:
    print "emp name is :",name
index=input("Enter index to print")
print "emp name at given index is: ",empname[index]
print "emp id at given index is: ",empid[index]
print empname[4:9]
print empname[3:]
count=input("enter number to repeate the list")
print empname*count
list3=empname + empid
print list3
for i in range(0,10):
    print "empname and emp id is ",empname[i],empid[i]
