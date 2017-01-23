count=input("Enter count number to print")
num=input("enter upper limit for fib")
a=0
b=1
fib=0
for ct in range(count):
    print fib
    a=b
    b=fib
    fib=a+b
fib=0
a=0
b=1
while fib < num :
     print fib
     a=b
     b=fib
     fib=a+b
