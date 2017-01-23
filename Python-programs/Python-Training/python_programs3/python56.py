try:
    fsize=input("file size")
    f=open("new.txt","r")	
    str1=f.read()
    x = int(raw_input("Please enter a number: "))
except IOError:
    print "file can not be opened please check if the file exist or not "
except ValueError:
    print "Oops!  That was no valid number.  Try again..."
else:
    print str1
