'''
my_set = {1, 2, 3}
print(my_set)
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
'''
'''
my_set = {1,2,3,4,3,2}
print(my_set)
my_set = set([1,2,3,2])
print(my_set)

a = {}
a = set()
print(type(a))
'''
'''
# change value
my_set = {1,3,2}
my_set.add(2)
print(my_set)

my_set.update([2,3,4])
print(my_set)

my_set.update([4,5], {1,6,8})
print(my_set)
'''
'''
# remove value
my_set = {1, 3, 4, 5, 6}
my_set.discard(4)
print(my_set)

my_set.remove(6)
print(my_set)
#remove use korle error asbe?
my_set.discard(2)
print(my_set)
'''
'''
my_set = set("HelloWorld")
print(my_set)

print(my_set.pop())

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)
'''
'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)
print(A & B)
print(A - B)
'''
'''
#Dictionary
myinfo = {'Name': 'Tran', 'Age': 37, 'Address': 'Vietnam'}
print ("mydict: ", myinfo)

mydict = dict()
mydict["E01"] = "John"
mydict["E02"] = "King"
mydict["E03"] = "Nasir"
mydict["E04"] = "Pallob"
mydict["E06"] = "Redu"
print ("mydict: ", mydict)

myinfo = {"Name": "Tran", "Age": 37, "Address" : "Vietnam" }
print ("myinfo['Name'] = ", myinfo["Name"])
print ("myinfo['Age'] = ", myinfo["Age"])
print ("myinfo['Address'] = ", myinfo["Address"])
'''
'''
#Update Dictionary
myinfo = {"Name": "Tran", "Age": 37, "Address" : "Vietnam" }

myinfo["Address"] = "HCM Vietnam"
myinfo["Phone"] = "12345"
myinfo["Prize"] = "$50"
print(myinfo)
print ("Element count: ", len(myinfo) )

print ("myinfo['Name'] = ", myinfo["Name"])
print ("myinfo['Age'] = ", myinfo["Age"])
print ("myinfo['Address'] = ", myinfo["Address"])
print ("myinfo['Phone'] = ", myinfo["Phone"])
print ("myinfo['prize'] = ", myinfo["Prize"])
'''
'''
#Delete
contacts = {"John": "01217000111", \
"Tom": "01234000111", \
"Addison":"01217000222", "Jack":"01227000123"}

print("contacts :",contacts)
print ("Delete key = 'John' ")
del contacts["John"]
print ("Contacts (After delete): ", contacts)
contacts.__delitem__( "Tom")
print ("Contacts (After delete): ", contacts)
print ("Clear all element")
contacts.clear()
print ("Contacts (After clear): ", contacts)
'''
contacts = {"John": "01217000111" ,"Addison": "01217000222","Jack": "01227000123"}
# print ("contacts: ", contacts)
# print ("Element count: ", len(contacts) )
contactsAsString = str(contacts)
print ("str(contacts): ", contactsAsString )

aType = type(contacts)
print ("type(contacts): ", aType )

#dict er mode ki ki ase ai gula amara use korte pari chile
print ("dir(dict): ", dir(dict) )


