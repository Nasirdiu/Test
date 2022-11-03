class AbstractDocument :
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class PDF(AbstractDocument):
        def show(self):
            print("Show PDF document:", self.name)
class Word(AbstractDocument):
    def show(self):
        print("Show Word document:", self.name)

documents = [ PDF("Python tutorial"),
        Word("Java IO Tutorial"),
        PDF("Python Date & Time Tutorial"),
        Word("Nasir Uddin") ]

for doc in documents :
    doc.show()