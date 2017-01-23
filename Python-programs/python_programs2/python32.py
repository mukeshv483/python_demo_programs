list1 = [1, 2, 3, 4, 5, 6, 7 ];
list2=[3,4,5,6,7,8,9,10]
list3=[11,21,13,14,15,6,16]
print "length of list1 is :",len(list1)
print "length of list2 is :",len(list2)
print "length of list3 is :",len(list3)
print "max in list1 is :",max(list1)
print "min in list1 is :",min(list1)
print "max in list2 is :",max(list2)
print "min in list2 is :",min(list2)
print "max in list3 is :",max(list3)
print "min in list3 is :",min(list3)
if cmp(list1, list2) == 1 and cmp(list1, list3) == 1:
    print "list1 is biggest"
if cmp(list2, list1) == 1 and cmp(list2, list3) == 1:
    print "list2 is biggest"
if cmp(list3, list1) == 1 and cmp(list3, list2) == 1:
    print "list3 is biggest"

if cmp(list1, list2) == -1 and cmp(list1, list3) == -1:
    print "list1 is smallest"
if cmp(list2, list1) == -1 and cmp(list2, list3) == -1:
    print "list2 is smallest"
if cmp(list3, list1) == -1 and cmp(list3, list2) == -1:
    print "list3 is smallest"
list1.pop(0)
list2.pop(0)
list3.pop(0)
list1.pop(len(list1)-1)
list2.pop(len(list2)-1)
list3.pop(len(list3)-1)
print "printing list after poping first and last element"
print "list1 is :", list1
print "list2 is :",list2
print "list3 is:",list3
