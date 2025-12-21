from typing import Tuple, List

class CanonicalHuffmanCodeGenerator():

    """
    Generates and stores canonical Huffman codes from a set of symbol code lengths.
    The class does not build a Huffman tree nor compute code lengths;
    it assigns bit patterns to symbols depending on its given code lengths.

    Since only bytes can be stored, and Huffman codewords have variable bit length
    each codeword is defined by an int, and a length, that is the number of bits that 
    we extract from the binary representation of that int.

    Since both Huffman compression and decompression will need the code, CanoncialHuffmanCodeGenerator
    generates two dictionaries, code (used for compression) and inverse_code (used for decompression). 
    Code uses the symbol to code as key, but inverse_code uses the tuple (number, length) as key.
    """

    def __init__(self, lengths):
        # lengths is a list of tuples containing (symbol, length)
        self.code = {}
        self.inverse_code = {}

        # Order the tuples prioritizing the lengths first.
        lengths.sort(key=lambda x: (x[1], x[0]))

        number = 0
        self.code[lengths[0][0]] = (number, lengths[0][1])

        self.inverse_code[(number, lengths[0][1])] = lengths[0][0]

        previous_length = lengths[0][1]


        for element in lengths[1:]:
            number = number + 1
            shift = element[1]-previous_length
            number <<= shift

            self.code[element[0]] = (number, element[1])
            self.inverse_code[(number, element[1])] = element[0]

            previous_length = element[1]