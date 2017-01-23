import sys
total = len(sys.argv)
arguements = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % arguements)
# qno5 b  part
total = len(sys.argv)
arguements = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % arguements)
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
if a==b and a==c:
    print "All the numbers are equal"
elif a>b and a>c:
  print " Greatest number is ",a
elif b>a and b>c:
    print "Greatest number is",b
else:
    print "Greatest number is",c
