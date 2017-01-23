def fib(num):
  a=0
  b=1
  fib=0
  for ct in range(num):
    print fib
    a=b
    b=fib
    fib=a+b

def findvalue(*var):
   list1=[1,2,3,4,5,6,6,7,7,8,9]
   for num in var:
      if num in list1:
         print "element is present and element is :",num

def chkpalindrome(var="maam"):
    rev_str = reversed(var)
    if list(var) == list(rev_str):
       print"Given string is palindrome is :",var
    else:
       print("It is not palindrome",var)


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


def extendtuple(list1,tuple1):
    tup=tuple(list1)
    tuple1=tup+tuple1
    print tuple1


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
def substr(str1,delimeter):
    sub=str1.split(delimeter)
    print sub


