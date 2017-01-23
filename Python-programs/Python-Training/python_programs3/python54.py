import time;
try:  
    for num in range(1,10):
        print num
        time.sleep(2)
    name = input ("Enter your name: ")
    print "your name is:",name
    a=input("enter range")
    b=100/0
except NameError:
    print "please define the variable before use "
except KeyboardInterrupt:
    print "execution is interrupted"
except ArithmeticError:  
        print "This statement is raising an exception"  
else:  
    print "Welcome"
