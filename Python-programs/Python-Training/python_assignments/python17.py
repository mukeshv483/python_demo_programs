numbers=[1,2,3,4,5,6,7,8,9,10]
minimum = None       
maximum = None

for num in numbers :                          
    if minimum == None or num < minimum :
        minimum = num

for num in numbers :        
    if maximum == None or maximum < num :
        maximum = num
print 'Maximum:', maximum
print 'Minimum:', minimum
print "maximum number is :",max(numbers)
print "minium number is :",min(numbers)
