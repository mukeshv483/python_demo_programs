def findmax(first=0,second=0,third=0,fourth=0):
    if((first>second) and (first>third) and (first>fourth)):
       print("First number is largest",first);
    elif((second>first) and (second>third) and (second>fourth)):
       print("Second number is largest",second);
    elif((third>second) and (third>first) and (third>fourth)):
        print("Third number is largest",third);
    elif((fourth>second) and (fourth>third) and (fourth>first)):
        print("Fourth number is largest",fourth);
    else:
         print "all numbers are equal"
f=input("enter number")
s=input("enter number")
t=input("enter number")
fou=input("enter number")
findmax(first=f,second=s,third=t,fourth=fou)
