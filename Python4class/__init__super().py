class Parent:
    def __init__(self):
        self.money = 10000
class Child(Parent):
    pass

class BadChild(Parent):
    def __init__(self):
        self.hobby = "게임"

class GoodChild(Parent):
    def __init__(self):
        super().__init__()
        self.hobby ="게임"

parent = Parent()
child = Child()
# badchild = BadChild()
goodchild = GoodChild()
print(parent.money)
print(child.money)
# print(BadChild.money)
print(goodchild.money)