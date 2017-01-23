tup1=(2,3,4,5,6,7,8,9,11,10)
tup2=(12,1,1,4,15,16,17,18,19)
if cmp(tup1,tup2)==1:
    print "tup1 is bigger than tup2"
elif cmp(tup1,tup2)==-1:
    print "tup2 is bigger than tup1"
else:
    print "tup1 is equal to  tup2"
print "length of tup1 is :",len(tup1)
print "length of tup2 is :",len(tup2)
print "max element in tup1 is :",max(tup1)
print "max element in tup2 is :",max(tup2)
print "min element in tup1 is :",max(tup1)
print "min element in tup2 is :",min(tup2)
print "converting tup1 and tup2 into list"
list1=list(tup1)
list2=list(tup2)
print list1
print list2
