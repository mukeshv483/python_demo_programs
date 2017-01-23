#a
print "reading file"
file = open("New1.txt", "r")
str1=file.read()
print str1
file.close()
#b
print "writing to the file"
file2 = open("New1.txt", "w")
for num in range(0,5):
  str2=raw_input("enter string to write to file")
  file2.write(str2)
file2.close()
print "writing complete"
#c
print "appending to the file"
file3 = open("New1.txt", "a")
for num in range(0,5):
  str2=raw_input("enter string to write to file")
  file3.write(str2)
file3.close()
print "appending complete"

print "finally reading file again to confirm "
file = open("New1.txt", "r")
str1=file.read()
print str1
file.close()
