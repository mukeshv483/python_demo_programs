import ListPackage as lp;
import TuplePackage as tp;
import FilePackage as fp;


dir1=raw_input("enter directory name i.e path ")

fp.searchpattern(dir1)

fillename=raw_input("enter file name i.e full path")

file=open(fillename,"r")

fp.reversecontent(file)
fp.writetofile()
empid=[1,2,3,4,5,6,7,8,9,10]
empname=["a","b","c","d","e","f","g","h","i","j"]
lp.printlist(empid)
lp.printlist(empname)
tuple1=tp.createweekday()
tp.printtuple(tuple1)