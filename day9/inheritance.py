class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class dancer:
    def __init__(self,style):
        self.style=style
class all(student,dancer):
    def __init__(self,age,name,style):
        student.__init__(self,name,age)
        dancer.__init__(self,style)
Nasir=all(20,"Nasir Uddin","Coder")
print(Nasir.name)
print(Nasir.age)
print(Nasir.style)



