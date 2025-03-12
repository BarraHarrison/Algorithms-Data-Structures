# Doubly-LinkedList: Data structure made up by a series of nodes
# Doubly-LinkedLists are used for caching, redoing functionality
# Two-Pointers (Forwards & Backwards)

class DNode:
    """A single node of a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None # Pointer
        self.prev = None # Pointer

class DoublyLinkedList:
    """Implementation of a doubly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        """Delete a node by its value."""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            temp = None
            return

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            return
        
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

        temp = None

    def display_forward(self):
        """Print all the nodes from the head to the tail."""
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")


    def display_backward(self):
        """Print all the nodes from the tail to the head."""
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("None")