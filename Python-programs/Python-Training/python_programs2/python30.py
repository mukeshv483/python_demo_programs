list1=[2,3,7,8,9,10,26,17,18] 
for i in range( len( list1 ) ):
    for k in range( len( list1 ) - 1, i, -1 ):
      if ( list1[k] < list1[k - 1] ):
        tmp = list1[k]
        list1[k] = list1[k-1]
        list1[k-1] = tmp
print list1 
