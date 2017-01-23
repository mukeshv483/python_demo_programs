a=input("Enter First Number")
b=input("Enter Second Number")
c=input("Enter Third Number")
if a==b and a==c:
    print "All the numbers are equal"
elif a>b and a>c:
  print " Greatest number is ",a
elif b>a and b>c:
    print "Greatest number is",b
else:
    print "Greatest number is",c
