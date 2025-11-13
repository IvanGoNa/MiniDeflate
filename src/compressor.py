from abc import abstractmethod
from abc import ABC

class Compressor(ABC):
    @abstractmethod
    def compress(self):
        pass

    @abstractmethod
    def decompress(self):
        pass