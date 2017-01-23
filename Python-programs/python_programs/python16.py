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
start = int(input("Enter lower range: "))
end = int(input("Enter upper range: "))

for num in range(start,end + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
