def ovals():
    ovals = 'aeiou'
    count = 0
    string = raw_input ("Enter a string: ")
    for i in string:
        if i in ovals:
            count += 1
    print "No. of ovals occurred", count
ovals()
