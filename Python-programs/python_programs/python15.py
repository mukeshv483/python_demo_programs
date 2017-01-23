empname=["mukesh","rahul","gaurav","abhisekh","lalit"]
str1="mukesh"
flag=0 
print str1 in empname
for str2 in empname:
  if str2 == str1:
      print "Given name Exist in the list"
      flag=1
if flag == 0:      
  print "Given number does not exist"     
empname.reverse()
print empname
