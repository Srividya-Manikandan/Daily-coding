"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""
nodes_dict = {}

# Return a unique 'address' for a given object
def get_pointer(node):
    return id(node) if node else 0

# Return the object stored at a given 'address'
def dereference_pointer(address, nodes_dict):
    return nodes_dict.get(address, None) if address != 0 else None

class XORNode:
    def __init__(self, value):
        self.value = value
        self.both = 0  # XOR of next and previous node addresses

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add an element to the end of the XOR linked list
    def add(self, element):
        new_node = XORNode(element)
        nodes_dict[get_pointer(new_node)] = new_node

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.both = get_pointer(self.tail) # New node's both points to the current tail
            self.tail.both ^= get_pointer(new_node) # Update current tail's both to include new node
            self.tail = new_node

        self.size += 1

    # Get the element at a specific index
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        prev_address = 0

        for _ in range(index):
            next_address = prev_address ^ current.both
            prev_address = get_pointer(current)
            current = dereference_pointer(next_address, nodes_dict)

        return current.value