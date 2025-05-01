from abc import ABC, abstractmethod


class VolumeCalculate(ABC):
    @abstractmethod
    def volume(self, *params):
        pass
