#inheritance 
class amber():
    def xyz(self):
        print("Parent class")
class asd(amber):
    super(amber)
def xyz(self):
    print("child class")
obj=asd()
obj.xyz()


class c1:
    def abc(self):
        print("parent class")
class c2(c1):
    def xyz(self):
        print("child class")
class c3(c1):
    def asd(self):
        print("child class")
obj=c2()
obj1=c3()
obj.abc()
obj.xyz()
obj1.abc()
obj1.asd()
class c1:
    def abc(self):
        print("parent class1")
class c2:
    def xyz(self):
        print("parent class2")
class c3(c1,c2):
    def amber(self):
        print("child class")
obj=c3()
obj.abc()
obj.xyz()
obj.amber()
a = ("okay!,Let`s play the game")
print=(a)


    
