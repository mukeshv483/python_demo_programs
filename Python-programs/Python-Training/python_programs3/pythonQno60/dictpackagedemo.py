import DictionaryPackage as dp;
dict1={"name":"mukesh","age":"21","dept":"cse"}
dict2={"course":"btech","company":"wipro","location":"bangalore"}
dict3={"name":"rahul","age":"21","dept":"cse"}
dict1["School"] = "mmm School"
dict2["program"]="python"
dp.cmpdict(dict1,dict2,dict3)
print dict1
print dict2
dp.dicttostr(dict1)
dp.dictlength(dict1)
dp.dictlength(dict2)
dp.concatdict(dict1,dict2)
dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}
dp.updatedict(dict1,dict2)
dp.isleapyear()
year=input("enter year to print calendar")
dp.printyearcal(year)