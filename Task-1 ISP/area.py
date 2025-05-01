from abc import ABC, abstractmethod

class AreaCalculate(ABC):
    @abstractmethod
    def area(self, *params):
        pass
