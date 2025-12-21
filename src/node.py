
class Node():
    
    """"
    Represents the node of a binary tree. Where a node can have a given value, and two
    child nodes. In this case each node contains a frequency value, in order to be used as a node by 
    HuffmanTree class.
    """

    def __init__(self, right_child=None, left_child=None, value=None, frequency=None):
        self.right_child = right_child
        self.left_child = left_child
        self.value = value
        self.frequency = frequency     

    def has_right_child(self):
        return (self.right_child != None)
    
    def is_leaf(self):
        return (self.left_child == None and self.right_child == None)
    
    def get_value(self):
        return self.value
    
