from day8player import Player
player1 = Player("Tom", 20)
player2 = Player("Jerry", 20)
print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)

print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)
print (" ------------ ")
print ("Assign new value to player1.age = 21 ")
# Assgin new value to age attribute of player1.
player1.age = 21

print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)
print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)