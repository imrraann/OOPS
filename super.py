class a():
    def __init__(self):
        print(" A")
    def display(self):
        print("You are in class A")
class b():
    
    def __init__(self):
        super().__init__()
        print(" B")
         
    def display(self,n,r):
        self.n=n
        self.__r=r
        print("You are in class B")

class c():
   
    def __init__(self):
        super().__init__()
        print(" c")
         
    def display(self):
        print("You are in class c")

A=b()
A.display(1,5)
print(A.__dir__)
