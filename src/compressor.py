from abc import abstractmethod
from abc import ABC

class Compressor(ABC):
    @abstractmethod
    def compress(self,data):
        pass

    @abstractmethod
    def decompress(self, compressed_data):
        pass
    
