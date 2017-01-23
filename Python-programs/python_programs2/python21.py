import math
import random
list = [20, 16, 10, 5];
a=input('Enter number: ')
print "Round Number of Floating Number: ", round(a) 
Sqroot=math.sqrt(a)
print "Square Root of the Number: ", Sqroot
print "Random Number between 0 and 1: ", random.random()
print "Random Number between 10  and 500: ", random.uniform(10,500)
print "Random choice from list : ", random.choice(list)
print "randrange between 100 to 500 : ", random.randrange(100, 500, 2)
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list
