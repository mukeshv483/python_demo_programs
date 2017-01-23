import os;
dirs = os.listdir(" ." )# current  directory 
pattern="Treasure"
count=0
for file in dirs:
    f=open(file,"r")
    str1=f.read()
    if pattern in str1:
       print "pattern occurred in file :",file
       count+=1
    f.close()
print "pattern occured in %d files" % count
for file in dirs:
    f=open(file,"r")
    str1=f.read()
    count1=str1.count(pattern,0,len(str1))
    f.close();
    print "occurrence of pattern in this file %s  is = %d :" %(file,count1)
