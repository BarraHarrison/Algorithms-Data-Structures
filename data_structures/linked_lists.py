# Linked-List: Data structure made up by a series of nodes
# Linked-Lists have dynamic-sizing which gives them an advantage over arrays
# One-Pointer to the next node

class Node:
    """A single node of a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Implementation of a linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Delete a node by its value."""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        
        prev.next = temp.next 
        temp = None

    def display(self):
        """Print all nodes on the list."""
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")


sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.display()

sll.delete_node(20)
sll.display()

# 10 → 20 → 30 → None
# 10 → 30 → None