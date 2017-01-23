def fib(num):
  a=0
  b=1
  fib=0
  for ct in range(num):
    print fib
    a=b
    b=fib
    fib=a+b
     
def add(num1,num2):
    sum1=num1 + num2
    print "sum is ",sum1
def sub(num1,num2):
    sub=num1 - num2
    print "subtraction is ",sub
def mul(num1,num2):
    mul=num1 * num2
    print "multiplication is ",mul
def div(num1,num2):
    div=num1 / num2
    print "division is ",div    
def sqrt(num):
     num_sqrt = num ** 0.5
     print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

def isprime(a):
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
