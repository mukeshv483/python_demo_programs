sum1=0
for num1 in range(1,11):
  num2=input("enter number")
  sum1=sum1+num2
average= sum1/10
print "average of the numbers are ",average  
#QNO-12(A,b,c)
sum1=0
list1=[0,0,0,0,0,0,0,0,0,0]
i=0
j=0
k=0
count=0

for num1 in range(1,11):
    list1[i]=input("Enter number")
    i=i+1
for num1 in range(1,11):    
   sum1=sum1+list1[j]
   j=j+1
average= sum1/10
print "average of the numbers are ",average
print list1
for k in range(0,10):
    if list1[k] > average:
       count=count+1
       print("value is greater then average",list1[k])
print "number of values greater than average is :",count
count=0   
for k in range(0,10):
    if list1[k] < average:
       count=count+1
       print("value is  less then average",list1[k])
print "number of values less than average is :",count
count=0
for k in range(0,10):
    if list1[k] == average:
       count=count+1
       print("value equal to average",list1[k])
print "number of values equal to average is :",count
