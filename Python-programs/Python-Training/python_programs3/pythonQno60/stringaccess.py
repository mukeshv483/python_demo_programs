import StringPackage as sp;
my_str = raw_input("Enter a string: ")
sp.ispalendrome(my_str)
string = raw_input ("Enter a string: ")
sp.countvowels(string)
list1=[2,3,7,8,9,10,26,17,18] 
sp.bubblesort(list1)
arr = [ 2, 3, 4, 10, 40 ]
x = 10
result = sp.binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
list1=[10,20,30,40,50,60,70]
print "enter index less than %d" %(len(list1))
sp.insertatindex(list1)