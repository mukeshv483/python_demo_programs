import sys;
import xyz;
try:
    num=input("press enter");
    10 * (1/0)
    x = int(raw_input("Please enter a number: "))
    f = open('myfile.txt')
    s = f.readline()
    print s
    sys.exit()
    list1=[1,2,3,4]
    print list1[12]
    a=10
    assert (a>100),"a must be greater than 100"

except SystemExit:
    print " SystemExit exception occured"
except StopIteration:
    print " StopIteration exception occured"
except OverflowError:
    print " OverflowErrorexception occured"
except FloatingPointError:
    print " FloatingPointError exception occured"
except AssertionError:
    print " AssertionError exception occured"
except AttributeError:
    print " AttributeError exception occured"
except EOFError:
    print " EOF exception occured"
except ImportError:
    print "ImportError exception occured"
except LookupError:
    print "LookupError exception occured"
except IndexError:
    print "IndexErrorexception occured"
except EnvironmentError:
    print "EnvironmentErrorexception occured"
except UnboundLocalError:
    print "UnboundLocalError exception occured"
except IndentationError:
    print " IndentationError exception occured"
except RuntimeError:
    print " RuntimeError exception occured"
except NotImplementedError:
    print " NotImplementedError exception occured"
except NameError:
    print "please define the variable before use "
except KeyboardInterrupt:
    print "execution is interrupted"
except IOError:
    print "IO exception occured"
except ArithmeticError:  
        print "This statement is raising an exception can not divide by zero"  
except ValueError:
        print "Oops!  That was no valid number.  Try again..."
except SyntaxError:
    print "SyntaxError exception occured"
except SystemError:
    print "SystemErrorexception occured"
except StandardError:
    print " StandardError exception occured"
