str = "this is simple string example...!!!";
print "str.capitalize() : ", str.capitalize()

print "str.center(60, 'a') : ", str.center(60, 'a')

sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)

str = str.encode('base64','strict');

print "Encoded String: " + str
print "Decoded String: " + str.decode('base64','strict')


#29.2:

str = "this is a\tsimple string example";

suffix = "is";
print str.endswith(suffix, 2, 4)
print str.endswith(suffix, 2, 6)

print "Original string: " + str
print "Defualt exapanded tab: " +  str.expandtabs()
print "Double exapanded tab: " +  str.expandtabs(16)

str1 = "exam";
print str.find(str1)
print str.find(str1, 10)
print str.find(str1, 40)

print str.index(str1)
print str.index(str1, 10)
print str.index(str1, 40)

str2="Bond007"  
print str2.isalnum()




#29.3:  
str="hello"
print str.isalpha()
strg="Hello World"
print strg.isalpha()

str1 = "123456";  
print str1.isdigit()

print str.islower()
print strg.islower()

str2 = u"bond007";  
print str2.isnumeric()
str3 = u"2007";
print str3.isnumeric()

str4 = "       "; 
print str4.isspace()
print str.isspace()







#29.4:

str = "This Is A Simple String Example"
print str.istitle()

str = "THIS IS A SIMPLE STRING EXAMPLE"; 
print str.isupper()

s = "/";
seq = ("12", "10", "1993");
print "DATE OF BIRTH: ", s.join( seq )

print "Length of the string: ", len(str)

print str.ljust(40, 'E')

#29.5:

str = "THIS IS A SIMPLE STRING EXAMPLE";

print str.lower()

str1 = "BBBBBBBthis is a simple string exampleBBBBBB";
print str1.lstrip('B')

print "Max character: " + max(str)

print "Min character: " + min(str)

from string import maketrans
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str2 = "this is a simple string example"
print str2.translate(trantab)


#29.6:

str = "this is string example....this is really string";
print str.replace("is", "was")
print str.replace("is", "was", 3)

str1 = "this is really a simple string example";
str2 = "is";
print str1.rfind(str2)
print str1.rfind(str2, 0, 10)

print str1.rindex(str2)
print str1.index(str2)

print str.rjust(50, 'R')


str3 = "mmmmmmmthis is string example....wow!!!mmmmmmm";
print str3.rstrip('m')

#29.7:
# Hello World program in Python
    
str = "Line1-1234 \nLine2-456 \nLine4-64789";
print str.split( )
print str.split(' ', 1 )


str1 = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str1.splitlines( )
print str1.splitlines( 0 )
print str1.splitlines( 3 )

str2 = "this is a simple string example...";
print str2.startswith( 'this' )
print str2.startswith( 'is', 2, 4 )

print str2.swapcase()

str3 = "BBBBthis is a simple string example BBBBBB";
print str3.strip( 'B' )



#29.7:

str = "this is a simple string example";
print str.title()

from string import maketrans  
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
print str.translate(trantab, 'xm')

print "string in Capital letters : ", str.upper()

print str.zfill(40)

str1 = u"Bond007";  
print str1.isdecimal();
str2 = u"23443434";
print str2.isdecimal();
