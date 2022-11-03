from rectangle import Rectangle
r1 = Rectangle(20, 10)
r2 = Rectangle(20 , 10)
r3 = r1

test1 = r1 == r2 # --> False
test2 = r1 == r3 # --> True

print ("r1 == r2 ? ", test1)
print ("r1 == r3 ? ", test2)

print (" -------------- ")
print ("r1 != r2 ? ", r1 != r2)#true
print ("r1 != r3 ? ", r1 != r3)#false