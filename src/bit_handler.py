

class BitWriter():

    """
    The BitWriter is used to manage bit insertions of length n in a byte array. Huffmann class uses it to
    insert the codeword that belongs to a specific value (byte). Since each value has a variable length codeword
    its insertions has to be done using a BitWriter.

    This BitWriter writes the most significant bit first.
    """
    
    def __init__(self):
        self.buffer = 0
        self.nbits = 0
        self.bytes = bytearray()

    def write(self, value : int, length : int):
        # Insert the value to the BitWriter buffer
        self.buffer = (self.buffer << length) | value
        self.nbits += length
        
        while self.nbits >= 8:
            self.nbits -= 8
            # Extract the 8 most significant bits
            byte = (self.buffer >> self.nbits) & 0xFF

            # Remove those bits from the buffer
            mask = (1 << self.nbits) - 1
            self.buffer = (self.buffer & mask)

            self.bytes.append(byte)

    def flush(self):
        padding = 0

        if self.nbits > 0:
            # Add 0 until the last byte is completed
            padding = 8 - self.nbits
            byte = (self.buffer << padding) & 0xFF
            self.bytes.append(byte)
            self.nbits = 0

        return self.bytes, padding

class BitReader():
    
    """ 
    The BitReader is used to read bit by bit from a given data or a whole byte if needed. 
    It is used by Huffman class to decompress the data, that has been written by a BitWriter.

    It reads the most significant bit first.
    """   

    def __init__(self, data, padding):
        self.data = data
        self.byte_index = 0
        self.bit_index = 0
        self.total_bits = len(data)*8 - padding

    def read_bit(self):
        if self.byte_index * 8 + self.bit_index >= self.total_bits:
            return None
        
        byte = self.data[self.byte_index]

        # Read the bit in bit_index position starting from the most significant bit
        bit = (byte >> (7 - self.bit_index)) & 1
        self.bit_index += 1

        if self.bit_index == 8:
            self.bit_index = 0
            self.byte_index += 1

        return bit
    
    def read_bytes(self, n_bytes):

        if self.byte_index * 8 + self.bit_index >= self.total_bits:
            return None
        
        remaining_bytes = (self.total_bits - (self.bit_index + self.byte_index*8))//8

        if n_bytes > remaining_bytes:
            raise ValueError(f"Trying to read {n_bytes} but only {remaining_bytes} are left")
        
        byte = self.data[self.byte_index : self.byte_index+n_bytes]
        self.byte_index += n_bytes

        return byte
    
    def read_remaining_bytes(self):
        """
        Reads all the remaining bytes only if the current bit to read is byte-aligned 
        That means bit_index == 0.
        """

        if self.bit_index != 0:
            raise ValueError("Reader not byte-aligned")
        
        return self.data[self.byte_index:]
    
    def restart(self):
        self.byte_index = 0
        self.bit_index = 0
        