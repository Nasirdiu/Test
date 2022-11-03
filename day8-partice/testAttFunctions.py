from player import Player
player1 = Player("Tom", 20)
print ("getattr(player1,'name') = " , getattr(player1,"name") )

print ("player1.age = ", player1.age)
setattr(player1,"age", 21)
print ("player1.age = ", player1.age)
hasAddress = hasattr(player1, "address")
print ("hasattr(player1, 'address') ? ", hasAddress)

print ("Create attribute 'address' for object 'player1'")
setattr(player1, 'address', "USA")
print ("player1.address = ", player1.address)

# Delete attribute 'address'.
delattr(player1, "address")