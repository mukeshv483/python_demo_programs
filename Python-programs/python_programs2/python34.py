list1 = [2,8,6,4,9,12,13]
list2=[3,4,5,7,8,9,10,29,23]
list3=[11,21,13,14,15,6,16]
largest = 0 
second_largest = 0 
for item in list1:
        if item > largest:
           second_largest = largest
           largest = item
        elif largest > item > second_largest:
            second_largest = item
l1max=[largest,second_largest]
largest = 0 
second_largest = 0 
for item in list2:
        if item > largest:
            second_largest = largest
            largest = item
        elif largest > item > second_largest:
            second_largest = item
l2max=[largest,second_largest]
largest = 0 
second_largest = 0 
for item in list3:
        if item > largest:
           second_largest = largest
           largest = item
        elif largest > item > second_largest:
            second_largest = item
l3max=[largest,second_largest]           
Maxlist=l1max+l2max+l3max
print "maxlist is :",Maxlist
sum1=0
for num in Maxlist:
    sum1=sum1+num
average=sum1/len(Maxlist)    
print "average of Maxlist is :",average

min1 =max(list1)
second_min = max(list1)-1
for item in list1:
        if item < min1:
            second_min = min1
            min1 = item
        elif min1 < item < second_min:
            second_min = item
l1min=[min1,second_min]
min1 = max(list2) 
second_min = max(list2)-1
for item in list2:
        if item < min1:
           second_min = min1
           min1 = item
        elif min1 < item < second_min:
            second_min = item
l2min=[min1,second_min]
min1 = max(list3) 
second_min = max(list3)-1  
for item in list3:
        if item < min1:
            second_min = min1
            min1 = item
        elif min1 < item < second_min:
            second_min = item
l3min=[min1,second_min]           
Minlist=l1min+l2min+l3min
print "minlist is :",Minlist
sum1=0
for num in Minlist:
    sum1=sum1+num
average=sum1/len(Minlist)    
print "average of Minlist is :",average
