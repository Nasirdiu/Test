from player import  Player
player1 = Player("Tom", 20)
player2 = Player("Jerry", 22)
print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)

print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)
print (" ------------ ")
print ("Assign new value to player1.age = 21 ")

player1.age = 40
player2.age=50
print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)
print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)