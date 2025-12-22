from src.compressor import Compressor
from collections import Counter
from src.node import Node
from src.huffman_tree import HuffmanTree
from src.code_generator import CanonicalHuffmanCodeGenerator
from src.bit_handler import BitReader, BitWriter



class Huffman(Compressor):
    """
    Responsible of compression and decompression using Huffman coding. In this implementation, canoncial 
    Huffman coding is used. 

    In order to be able to decompress, the compress data has the following strutcture:

    data:  [size of lengths information] [lengths information] [padding used] [    data  |  padding ]

    sizes: [           1 byte          ] [     n bytes       ] [   1 byte   ] [ n' bytes | n'' bytes]

    Since we are using canonical Huffman, only lengths information is needed to recover the code that
    was used to encode the data. Lengths information has teh following structure:

    [symbol_1 | length_1 | symbol_2 | length_2 | .... | symbol_n | length_n] (each 1 byte)

    """
    def __init__(self):
        self.bit_writer = BitWriter()

    def compress(self,data):

        frequencies = Counter(data)

        # Generate Nodes
        nodes = [Node(value=key, frequency=value) for key, value in frequencies.items() ]

        # Generate Huffman code
        code, lengths = self._generate_code(nodes)

        # Code data and write it to our bitWriter
        for byte in data:
            bits, length = code[byte]
            self.bit_writer.write(bits, length)

        # End writing 
        compressed_data, padding = self.bit_writer.flush()

        # Compress the code used
        compressed_lengths = self._compress_lengths(lengths)

        # Merge all the info
        merged_data = bytearray()
        merged_data.extend(compressed_lengths)
        merged_data.extend(padding.to_bytes(1))
        merged_data.extend(compressed_data)
        return merged_data


    def decompress(self, compressed_info):
        decompressed = bytearray()
        code, padding, data = self._deserialize(compressed_info)
        bit_reader = BitReader(data, padding)

        length = 1
        number = 0

        while (bit:=bit_reader.read_bit()) != None:
            number = (number << 1) | bit

            if (number, length) in code:
                decompressed.append(code[(number, length)])
                length = 1
                number = 0
            else:
                length += 1

        return decompressed
    
    
    def _deserialize(self, data):
        reader = BitReader(data,0)

        lengths_size = int.from_bytes(reader.read_bytes(2), "big")
        lengths = reader.read_bytes(lengths_size)

        code = self._reconstruct_code(lengths)

        padding = int.from_bytes(reader.read_bytes(1), "big")
        data = reader.read_remaining_bytes()
        
        return (code, padding, data)
    
    def _compress_lengths(self, lengths):

        compressed_length = bytearray()

        for element in lengths:
            symbol, length = element
            compressed_length.extend(symbol.to_bytes(1,"big"))
            compressed_length.extend(length.to_bytes(1, "big"))

        lengths_size = len(compressed_length)
        length_bytes = lengths_size.to_bytes(2, "big")
        data = bytearray()
        data.extend(length_bytes)
        data.extend(compressed_length)
        
        return data
    
    def _reconstruct_code(self, lengths):
        reader = BitReader(lengths, 0)
        extracted_lengths = []

        while symbol:=reader.read_bytes(1):
            length = reader.read_bytes(1)
            extracted_lengths.append((int.from_bytes(symbol), int.from_bytes(length)))

        codeGenerator = CanonicalHuffmanCodeGenerator(extracted_lengths)
        return codeGenerator.inverse_code

    def _generate_code(self, nodes):
        huffman_tree = HuffmanTree(nodes)
        huffman_tree.generate_code(huffman_tree.root_node)
        return huffman_tree.code, huffman_tree.lengths

