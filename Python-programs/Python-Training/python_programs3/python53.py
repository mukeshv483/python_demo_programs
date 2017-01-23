file1=open("New.txt","w+")
str3=raw_input("enter string to write to file")
file1.write(str3)
string="""Opens a file for both appending and reading. The file pointer is at the end of the file
if the file exists The file opens in the append mode. 
If file does not exist, it creates a new file for reading and writing."""
list1=["mukesh","verma","gaurav","rawat","rahul","lalit"]
file1.writelines(list1)
file1.write(string)
file1.close()
file=open("New.txt","r")
print "file number is ",file.fileno()
str1=file.readline()
print "first line of file"
print str1
print "current pointer position is",file.tell()
file.seek(0,0)
print "current pointer position is",file.tell()
lines=file.readlines()
print "current pointer position is",file.tell()
print "printing file line by line"
for line in lines:
    print line
    
print file.isatty()
file.seek(0,0)
for line in range(len(lines)):
    print file.next()
file.close()
