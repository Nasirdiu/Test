booklist = []
print("1. ADD Book")
print("2. Display all Book")
print("3. Edit/Update Book")
print("4. DELETE book")
print("5. Search book")
print("1. exit")
while True:
    print("select your menu")
    print("=================")
    menu = input("Enter menu :")
    if menu =="1":
        print("you can add Book")
        print("=================")
        while True:
            userinput = input("Book name:")
            if userinput == "6":
                break
            booklist.append(userinput)
    elif menu =="2":
        print("list of Book")
        print("=============")
        while True:
            for x in booklist:
                print(x)
            userinput = input("exit:")
            if userinput == "6":
                break
    elif menu =="3":
        print("update Book")
        print("===========")
        while True:
            print(booklist)
            userinput = input("search:")
            if userinput in booklist:
                indexNum = booklist.index(userinput)
                booklist[indexNum] =input("new value :")
            else:
                print("no search result found")
            if userinput == "6":
                break
    elif menu =="4":
        print("Delete Book")
        print("===========")
        while True:
            print(booklist)
            userinput = input("search:")
            if userinput in booklist:
                indexNum = booklist.index(userinput)
                del booklist[indexNum]
                print("delete data")
            else:
                print("no search result found")
            if userinput == "6":
                break
    elif menu =="5":
        print("Search Book")
        print("===========")
        while True:
            userinput = input("search by book name:")
            if userinput in booklist:
                indexNum = booklist.index(userinput)
                print("Found :",booklist[indexNum])
            else:
                print("no search result found")
            if userinput == "6":
                print("exit the search page")
                break
    else:
        print("Sorry no menu item you selected")
        if userinput == "6":
            break
        print("exit")