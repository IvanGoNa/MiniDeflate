from src.node import Node
from typing import List
from src.code_generator import CanonicalHuffmanCodeGenerator

class HuffmanTree():

    """
    Generates and stores the Huffman Tree used to calculate the codeword length
    for each symbol. 

    The code used has been extracted and adapted from W3Schools:
    https://www.w3schools.com/dsa/dsa_ref_huffman_coding.php
    """

    def __init__(self, nodes : List[Node]):
        while len(nodes)>1:
            nodes.sort(key=lambda x: x.frequency)
            left=nodes.pop(0)
            right=nodes.pop(0)

            merged_node = Node(frequency=left.frequency + right.frequency)
            merged_node.left_child = left
            merged_node.right_child = right 

            nodes.append(merged_node)

        self.root_node = nodes[0]
        self.lengths = []
    
    def generate_code(self, current_node : Node):  
        self._calculate_lengths(current_node, 0)
        codeGenerator = CanonicalHuffmanCodeGenerator(self.lengths)
        self.code = codeGenerator.code
        self.inverse_code = codeGenerator.inverse_code

    def _calculate_lengths(self, current_node : Node, current_length):
        if current_node is None:
            return
    
        if current_node.value is not None:
            self.lengths.append((current_node.value, current_length))

        self._calculate_lengths(current_node.left_child, current_length + 1)
        self._calculate_lengths(current_node.right_child , current_length + 1 )