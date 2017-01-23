def fib(num):
  a=0
  b=1
  fib=0
  for ct in range(num):
    print fib
    a=b
    b=fib
    fib=a+b
count=input("Enter count number to print")
fib(count)
