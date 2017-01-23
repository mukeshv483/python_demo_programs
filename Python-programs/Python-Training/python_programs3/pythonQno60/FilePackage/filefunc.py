import os;

def readfile(file1):
  file = open(file1, "r")
  print "reading file"
  str1=file.read()
  print str1
  file.close()
def writetofile(file1):
    file = open(file1, "w")
    print "writing to the file"
    for num in range(0,5):
       str2=raw_input("enter string to write to file")
       file.write(str2)
    file.close()
    print "writing complete"
def appending(file1):
    print "appending to the file"
    file3 = open(file1, "a")
    for num in range(0,5):
        str2=raw_input("enter string to write to file")
        file3.write(str2)
    file3.close()
    print "appending complete"

def searchpattern(directory):
    pattern=raw_input("enter pattern to search")
    dirs = os.listdir(directory)  
    count=0
    for file in dirs:
      f=open(directory+"/"+file,"r")
      str1=f.read()
      if pattern in str1:
        print "pattern occurred in file :",file
        count+=1
      f.close()
    print "pattern occured in %d files" % count
    for file in dirs:
        f=open(directory+"/"+file,"r")
        str1=f.read()
        count1=str1.count(pattern,0,len(str1))
        print "occurrence of pattern in this file %s  is = %d :" %(file,count1)
        f.close();
    

def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

def revlineorder(file):
    file=open(file,"r")
    str1=file.readlines()
    count=len(str1)-1
    for line in str1:
      print str1[count]
      count=count-1   
      file.close()
def reversecontent(file):
    file=open(file,"r")
    str3=reverse(file.read())
    file.close();
    print str3




