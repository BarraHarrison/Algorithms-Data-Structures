# AVL Tree: Type of Self-Balancing Binary Search Tree
# Self-Balancing Trees re-balance themselves in logarithmic time
# The height differences between the subtrees is at most 1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        """Returns the height of the node"""
        return node.height if node else 0

    def get_balance_factor(self, node):
        """Returns the balance factor of the node"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        """Performs a right rotation"""
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x):
        """Performs a left rotation"""
        y = x.right
        T2 = y.left

        y.left = y
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node, value):
        """Recursively inserts a value and balances the tree"""
        if not node:
            return Node(value)

        if value < node.value:
             node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        balance = self.get_balance_factor(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def inorder_traversal(self, node, result=None):
        "Returns a sorted order"
        if result is None:
            result = []

        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

        return result

    def insert_value(self, value):
        """Insert values starting from the root"""
        self.root = self.insert(self.root, value)


avl = AVLTree()
values = [10, 20, 30, 40, 50, 25]
for val in values:
    avl.insert_value(val)

print("AVL Tree Inorder Traversal (Sorted Order):", avl.inorder_traversal(avl.root))