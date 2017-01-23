import time;
localtime=localtime = time.asctime( time.localtime(time.time()))
for num in range(0,60,5):
    print "current time is:",localtime
    time.sleep(5)

#b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.
 start=time.time()
list1 = [1, 2, 3, 4, 5, 6, 7 ];
list2=[3,4,5,6,7,8,9,10]
list3=[11,21,13,14,15,6,16]
print "length of list1 is :",len(list1)
print "length of list2 is :",len(list2)
print "length of list3 is :",len(list3)
end=time.time()
print "total cpu time in execution in seconds is :",end-start

