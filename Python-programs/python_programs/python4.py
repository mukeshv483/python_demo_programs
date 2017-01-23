a=input("Enter First Number")
b=0
if a>1:
     
    for i in range(2,a):
       if (a % i) == 0:
        b=b+1   
        print  "given number is not a prime number",a
        break
    if b<1:
        print "Given number is  a prime number",a    
else:
    print "Given number is not a prime number",a
