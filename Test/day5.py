'''
fruitTuple = ('apple', 'apricot', 'banana', 'coconut', 'lemen')
otherTuple = (100, "one", "two", 3)
print ("Fruit Tuple:")
print(fruitTuple)
print (" --------------------------- ")
print ("Other Tuple:")
print (otherTuple)

'''
'''
list1 = [1990, 1991, 1992]
print ("list1: ", list1)

list1Address = hex ( id(list1) )
print ("Address of list1: ", list1Address )

print ("\n")
print ("Append element 2001 to list1")
list1.append(2001)
print ("list1 (After append): ", list1)

list1Address = hex ( id(list1) )
print ("Address of list1 (After append): ", list1Address )
'''

'''
tuple1 = (1990, 1991, 1992)
tuple1Address = hex ( id(tuple1) )
print ("Address of tuple1: ", tuple1Address )
tuple1 = tuple1 + (2001, 2002)
tuple1Address = hex ( id(tuple1) )
print ("Address of tuple1 (After concat): ", tuple1Address )
'''
'''
fruits = ("apple", "apricot", "banana", "coconut", "lemen", "plum", "pear")
for fruit in fruits :
    print ("Fruit: ", fruit)

fruits = ("apple", "apricot", "banana", "coconut", "lemen", "plum", "pear")
print ( fruits )
print ("Element count: ", len(fruits) )
for i in range (0, len(fruits) ) :
    print ("Element at ", i, "= ", fruits[i] )

subTuple = fruits[1: 4]
print ("Sub Tuple [1:4] ", subTuple )

'''

'''
fruits = ("apple", "apricot", "banana", "coconut", "lemen", "plum", "pear")
print ("Element count: ", len(fruits) )
print ("fruits[-1]: ", fruits[-7])
print ("fruits[-2]: ", fruits[-2])
subTuple1 = fruits[-4: ]
print ("Sub Tuple fruits[-4: ] ")
print (subTuple1)
subTuple2 = fruits[-4:-2]
print ("\n")
print ("Sub Tuple fruits[-4:-2] ")
print (subTuple2)
'''
'''
tuple1 = (1990, 1991, 1992)
print ("tuple1: ", tuple1)
print ("Concat (2001, 2002) to tuple1")
tuple2 = tuple1 + (2001, 2002)
print ("tuple2: ", tuple2)
tuple3 = tuple2[1:4]
print ("tuple2[1:4]: ", tuple3)
tuple4 = tuple2[1: ]
print("tuple4 :",tuple4)
'''
'''
tuple1 = (1, 2, 3)
tuple2 = ("One", "Two")

tuple12 = tuple1 + tuple2
print ("tuple1 + tuple2: ", tuple12)
tuple2x3 = tuple2 * 3
print ("tuple2 * 3: ", tuple2x3)

hasThree = "Three" in tuple2
print ("'Three' in tuple2? ", hasThree)
'''
'''
tuple1 = (1991, 1994, 1992)
tuple2 = (1991, 1994, 2000, 1992)
print ("len(tuple1): ", len(tuple1) )
print ("len(tuple2): ", len(tuple2) )
maxValue = max(tuple1)
print ("Max value of tuple1: ", maxValue)
minValue = min(tuple1)
print ("Min value of tuple1: ", minValue)

list3 = [2001, 2005, 2012]
print ("list3: ", list3)
tuple3 = tuple (list3)
print ("tuple3: ", tuple3)
'''
years = ( 1990 , 1991 , 1993 , 1991 , 1993 , 1993 , 1993 )
print ("years.count(1993): ",years.count(1993) )
print ("years.index(1993): ", years.index(1993) )
print ("years.index(1993, 3): ", years.index(1993, 3) )
print ("years.index(1993, 4, 6): ", years.index(1993, 1, 6) )