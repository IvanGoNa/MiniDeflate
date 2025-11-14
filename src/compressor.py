from abc import abstractmethod
from abc import ABC

class Compressor(ABC):
    @abstractmethod
    def compress(self):
        pass

    @abstractmethod
    def decompress(self):
        pass
    
    @abstractmethod
    def read(self,filename):
        pass

    @abstractmethod
    def write(self, filename, data):
        pass