from abc import ABC,abstractmethod
class vehicle(ABC):
    def __init__(self,n):
       self.n=n
    
    def start(self):
        pass

v=vehicle(1)