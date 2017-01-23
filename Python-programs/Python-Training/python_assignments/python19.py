list1=[10,20,30,40]
list1=[10,20,30,40,50]
for num in range(1,100):
    if num == 50:
        break
    if num%2 != 0:
       continue
    elif num in list1: 
        continue
    else:
        print num
    
count = 2    
list1=[60,70,80,90]
while count < 100:
    count+=1
    if count == 90:
        break
    if count%2 != 0:
       continue
    elif count in list1: 
        continue
    else:
        print count
