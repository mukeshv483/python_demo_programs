file = open("New/New1.txt", "r")
str1=file.read(10)
count=10
while len(str1) != 0 :
   str1=file.read(10)
   print str1
   count+=10
   if count == 100:
    print "cursor position before resetting",file.tell()
    print "resetting the cursor to start of the file"   
    file.seek(0, 0)
    break
print "checking seek value and printing from start"
print "current cursor position is :",file.tell()
str2=file.read(10)
print str2
file.close()

file1 = open("New/New1.txt", "r")
for line in range(4):
   file1.readline()
print "printing from line 5th and onwards"
print file1.read()
file1.close()
