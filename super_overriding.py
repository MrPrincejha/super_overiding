class A:
    classvar = "i am classvar in class A"
    def __init__(self):
        self.var = "i am in class A's constructor"
        self.classvar = "instance var in class a"
        self.special = "special"

class B(A):
    classvar = "i am classvar in class B"
    def __init__(self):
        super().__init__()
        self.var = "i am in class B's constructor"
        self.classvar = "instance var in class B"
        print(super().classvar)
a = A()
b = B()

print(b.classvar)
# print(b.special) overring is necessary to access it