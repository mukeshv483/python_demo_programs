def ispalendrome(str1):
    rev_str = reversed(str1)
    if list(str1) == list(rev_str):
        print("It is palindrome")
    else:
         print("It is not palindrome")
         
def countvowels(string):
    vowels= 'aeiou'
    count = 0
    a=0
    e=0
    i=0
    o=0
    u=0
    for ch in string:
        if ch in vowels:
            count += 1
        if ch =='a' or ch=='A':
            a+=1
        if ch =='e' or ch=='E':
            e+=1
        if ch =='i' or ch=='I':
            i+=1
        if ch =='o' or ch=='O':
            o+=1
        if ch =='u' or ch=='U':
            u+=1
    print "No. of vowels occurred", count
    print "count of a is ",a
    print "count of a is ",e
    print "count of a is ",i
    print "count of a is ",o
    print "count of a is ",u

def bubblesort(list1):
    for i in range( len( list1 ) ):
        for k in range( len( list1 ) - 1, i, -1 ):
            if ( list1[k] < list1[k - 1] ):
             tmp = list1[k]
             list1[k] = list1[k-1]
             list1[k-1] = tmp
    print "sorted list is"
    print list1 

def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l)/2;
        if arr[mid] == x:
            return mid
 
        elif arr[mid] < x:
            l = mid + 1
 
        else:
            r = mid - 1

    return -1

def insertatindex(list1):
    index=input("enter index ")
    value=input("enter value to insert")
    list1.insert(index,value)
    print "element  %d is inserted  at index %d" %(value,index)
        
def reversesort(list1):
    list1.sort( reverse=True)
    print"desending order sorted list is :",list1

 
