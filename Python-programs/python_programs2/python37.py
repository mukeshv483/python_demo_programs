dict1={"name":"mukesh","age":"21","dept":"cse"}
dict2={"course":"btech","company":"wipro","location":"bangalore"}
dict3={"name":"rahul","age":"21","dept":"cse"}
if cmp(dict1,dict2)==1 and cmp(dict1,dict3)==1:
    print "dict1 is biggest"
if cmp(dict2,dict1)==1 and cmp(dict2,dict3)==1:
    print "dict2 is biggest"
if cmp(dict3,dict1)==1 and cmp(dict3,dict2)==1:
    print "dict3 is biggest"    
if cmp(dict1,dict2)==0 and cmp(dict1,dict3)==0:
    print "all are equal"
dict1["School"] = "mmm School"
dict2["program"]="python"
print dict1
print dict2
print "length of dict1 is:",len(dict1)
print "length of dict2 is:",len(dict2)
print "length of dict3 is:",len(dict3)
print "converting dictionary into string"
str1=str(dict1)
str2=str(dict2)
str3=str(dict3)
print str1
print str2
print str3
finalstr=str1+str2+str3
print "final string after concatination",finalstr
