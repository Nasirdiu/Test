from day8player import Player
player1 = Player("Tom", 20)
player2 = Player("Jerry", 20)

#player1.address = "USA"
#player2.address="UK"

print ("player1.name = ", player1.name)
print ("player1.age = ", player1.age)
print ("player1.address = ", player1.address)
print (" ------------------- ")
print ("player2.name = ", player2.name)
print ("player2.age = ", player2.age)
# player2 has no attribute 'address' (Error!!)
print ("player2.address = ", player2.address)