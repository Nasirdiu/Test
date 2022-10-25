#def functionName( parameters ):
'''
def sayHello(name) :
    if not name:
        print("Hello every body!")
    else:
        print("Hello " + name)

sayHello("")
sayHello("Python");
sayHello("Java");
'''
'''
def getGreeting(name) :
    if not name:
        return "Hello every body!"
    return "Hello " + name
greeting = getGreeting("")
print(greeting)

greeting = getGreeting("Python")
print(greeting)
'''
'''
def showInfo(name, gender):

    print("Name: ", name);
    print("Gender: ", gender);

showInfo("Tran", "Male")
showInfo("Tran","plan")
'''
'''
def showInfo(name, gender = "Male", country ="US"):
    print("Name: ", name)
    print("Gender: ", gender)
    print("Country: ", country)
    
showInfo("Aladdin", "Male", "India")
showInfo("Tom", "Male")
print(" ------ ")
showInfo("Jerry")
print(" ------ ")
showInfo(name="Tintin", country="France")
print(" ------ ")
'''
def sumValues(a, b, *others):
    number = a + b
    for other in others:
        number = number + other
    return number

a = sumValues(10, 20)
print("sumValues(10, 20) = ", a);

a = sumValues(10, 20, 1);
print("sumValues(10, 20, 1 ) = ", a);

a = sumValues(10, 20, 1, 2);
print("sumValues(10, 20, 1 , 2) = ", a);

a = sumValues(10, 20, 1, 2,3,4,5);
print("sumValues(10, 20, 1, 2, 3, 4, 5) = ", a);


