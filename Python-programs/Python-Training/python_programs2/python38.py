dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
dict1.update(dict2)
print dict1
dict1['Salary']=5000+500
print dict1
dict1['Age']=26
print dict1
dict1['grade']="B1"
print dict1
keys= dict1.keys()
values= dict1.values()
print "keys are:"
for key in keys:
    print key
print "values are :"
for value in values :
    print value
del dict1["Age"]
print dict1
