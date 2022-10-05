# a=5;b=10
# if a<b:
#     print("Hello World")

# a=5 ; b=10
# if a<b and a>0:
#     print("a is smaller than b but greater than 0")

# a=10 ;b=5
# if a<b:
#     print("a is smaller than b")
# else:
#     print("a is greater than b")

# a=10
# if a==0:
#     print("zero")
# elif a>0:
#     print("Posstive Number")
# else:
#     print("Negtive Number")

user="nasir"
password=1234
verification=12

userName=input("Enter Your Name :")

if userName==user:
    userPassword =int(input("Enter Your Password :"))
    if userPassword == password:

        verifica_tion=int(input("Enter verification code :"))
        if verification==verifica_tion:
            print('success')
        else:
            print('worng')
    else:
        print("worng password")
else:
    print("worng UserName")



