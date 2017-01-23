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

add(12,36)
sub(36,12)
mul(12,36)
div(36,12)
num = float(input('Enter a number: '))
sqrt(num)
substr("Pack: My: Box: With: Good: Food",":")
