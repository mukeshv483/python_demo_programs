def reverse(string):
begin = 0
end = len(string) - 1
strlist = [i for i in string]
while(begin < end):
temp = strlist[begin]
strlist[begin] = strlist[end]
strlist[end] = temp
begin += 1
end -= 1
return ''.join(strlist)
def bubbleSort(alist):
for passnum in range(len(alist)-1,0,-1):
for i in range(passnum):
if alist[i]>alist[i+1]:
temp = alist[i]
alist[i] = alist[i+1]
alist[i+1] = temp
def binarySearch(alist, item):
first = 0
last = len(alist)-1
found = False
while first<=last and not found:
midpoint = (first + last)//2
if alist[midpoint] == item:
found = True
else:
if item < alist[midpoint]:
last = midpoint-1
else:
first = midpoint+1
return found
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
print reverse('flash')
