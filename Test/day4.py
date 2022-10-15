
'''
fruitList = ['apple', 'apricot', 'banana', 'coconut', 'lemen']

otherList = [100, 'one', 'two', 3]
print (fruitList)
print (otherList)

'''
'''
fruitList = ['apple', 'apricot', 'banana', 'coconut', 'lemen']

for fruit in fruitList :
    print("Fruit",' - ',fruit)
'''
'''
fruitList = ['apple', 'apricot', 'banana', 'coconut', 'lemen']
subList = fruitList[2:4]
print(subList)
'''

'''
#Append
fruitList = ['apple', 'apricot', 'banana', 'coconut', 'lemen']
subList = fruitList[-2:-1]
print(subList)
'''
'''
years = [1991,1995, 1992]
print ("Years: ", years)
years[1] = 2000
print ("Years: ", years)
print ( years )
years.append( 2015 )
years.append( 2022 )
print ( years )
'''
'''
# slice
years = [ 1990 , 1991 , 1992 , 1993 , 1994 , 1995 , 1996 ]
years[1:5] = [ 2000 , 2001 ]
print ("Years: ", years)

'''
''' 
#Delete
years = [ 1990 , 1991 , 1992 , 1993 , 1994 , 1995 , 1996 ]
#del years[6]
del years[1:4]
print(years)
'''
'''
#remove(value)
years = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
years.remove(6)
print ("Years: ", years)
'''

'''
list1 = [1, 2, 3]
list2 = ["One", "Two"]
list12 = list1 + list2
print(list12)
list2x3 = list2 * 3
print ("list2 * 3: ", list2x3)

hasThree = "One" in list2
print ("'Three' in list2? ", hasThree)
'''
'''
#min max lenth list
list1 = [1, 2, 3]
list2 = ["One", "Two"]
list3=len(list1)
print(list3)
'''
years = [ 1990 , 1991 , 1992 , 1993 , 1993 , 1993 , 1994 ]
print ("Years: ", years)
# Reverse the list.
years.reverse()
print ("Years (After reverse): ", years)