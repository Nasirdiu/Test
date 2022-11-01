
# Rectangle.

class Rectangle :

    def __init__(self, width, height):
        self.width= width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
# Method to calculate Area.
    def getArea(self):
        return self.width * self.height
r1 = Rectangle(10,5)
r2 = Rectangle(20,11)

print ("r1.width = ", r1.width)
print ("r1.height = ", r1.height)
print ("r1.getWidth() = ", r1.getWidth())
print ("r1.getArea() = ", r1.getArea())
print ("-----------------")
print ("r2.width = ", r2.width)
print ("r2.height = ", r2.height)
print ("r2.getWidth() = ", r2.getWidth())
print ("r2.getArea() = ", r2.getArea())
print ("Exit rectangle -------------- ")

