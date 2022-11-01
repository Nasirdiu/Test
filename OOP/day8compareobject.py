from day8rectangle import Rectangle
r1 = Rectangle(20, 10)
r2 = Rectangle(20 , 10)
r3 = r1
# Compare the address of r1 and r2
test1 = r1 == r2
# Compare the address of r1 and r2
test2 = r1 == r3

print ("r1 == r2 ? ", test1)
print ("r1 == r3 ? ", test2)
print (" -------------- ")
print ("r1 != r2 ? ", r1 != r2)
print ("r1 != r3 ? ", r1 != r3)