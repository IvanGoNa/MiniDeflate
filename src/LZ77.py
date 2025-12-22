
from src.compressor import Compressor

"""
LZ77 is a lossless compression algorithm that replaces sequences of repeated bytes with references to them.
It generates tuples that follow the structure (distance, length, next_byte). 
In this implementation distance and length are stored using 2 bytes each, and next_byte uses 1 byte.
"""
class LZ77(Compressor):
    TUPLE_SIZE = 5
    LAB_LENGTH = 32000
    SB_LENGTH = 32000
    N_BYTES_FOR_INTEGERS = 2
    N_BYTES_FOR_ELEMENTS = 1

    def compress(self, info):

        search_buffer= bytearray()
        look_ahead_buffer = info[0:self.LAB_LENGTH] 
        tuples = []

        n_byte = 0; 
        while n_byte < len(info):
            
            next_byte = info[n_byte]
            distance = 0
            length = 0
            
            #If the byte next_byte is not in the search buffer we append (0,0,next_byte) 
            if next_byte in search_buffer:
                #We find the longest coincident sequence of the search buffer that imitates
                #the beginning of the look_ahead_buffer. 
                beginning, length = self._length_of_longest_coincident_sequence(search_buffer, look_ahead_buffer)      
                distance = len(search_buffer)-beginning
                next_byte = info[n_byte+length]  if (n_byte+length) < len(info) else None

            #We add to the search buffer those bytes present in the sequence found (if found)
            for i in range(0, length+1):
                    if (n_byte + i) < len(info):
                        search_buffer.append(info[n_byte+i])

            n_byte += length + 1
            search_buffer = search_buffer[-self.SB_LENGTH:]
            look_ahead_buffer = info[n_byte: n_byte+self.LAB_LENGTH]

            tuple = (distance, length, next_byte)
            tuples.append(tuple)

        return self._serialize(tuples)

    def decompress(self, compressed):
        decompressed = bytearray()
        for token in compressed:
            distance, length, next_byte = token
            #If length > 0, we copy length elements from the decompressed buffer, starting distance positions backwards.
            for _ in range(0,length):
                decompressed.append(decompressed[-distance])
            
            if next_byte != None:
                decompressed.append(next_byte)

        return decompressed
    
    def write(self, filename, compressed_data):
         with open(filename, "wb") as file:
            file.write(compressed_data)

    def read(self, filename):

        with open(filename, "rb") as file:
            compressed_data = []
            while True:
                token = file.read(self.TUPLE_SIZE)
                #We read until no more tuples are left
                if len(token) < self.TUPLE_SIZE - 1:
                    break
                distance = int.from_bytes(token[0:2], "big")
                length = int.from_bytes(token[2:4], "big")

                try:
                    next_byte = token[4]
                except IndexError:
                    next_byte = None

                compressed_data.append((distance, length, next_byte))
        
        return compressed_data

    def _length_of_longest_coincident_sequence(self, search_buffer, look_ahead_buffer):

        maximum_length = 0
        beginning_index = 0

        for length in range(0,len(look_ahead_buffer)):
                #Find the last position in search_buffer where the first length bytes of look_ahead_buffer appear.
                start_index = search_buffer.rfind(look_ahead_buffer[0:length])   
                if start_index != -1:
                    maximum_length = length
                    beginning_index = start_index
                else:
                    break

        return beginning_index, maximum_length
    
    def _serialize(self, tuples):
        compressed = bytearray()

        for distance, length, next_byte in tuples:
                #We use 2 bytes for distance_to_begginning and length
                #We are representing bytes as integers --> to_bytes(...)
                compressed.extend(distance.to_bytes(self.N_BYTES_FOR_INTEGERS,'big'))
                compressed.extend(length.to_bytes(self.N_BYTES_FOR_INTEGERS,'big'))
                if next_byte is not None:
                    compressed.extend(next_byte.to_bytes(self.N_BYTES_FOR_ELEMENTS,'big'))


        return compressed