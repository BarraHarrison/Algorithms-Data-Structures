# B*-Tree is an optimized version of a B-Tree
# Splits nodes less often and ensures a higher % of node occupancy

class BStarTreeNode:
    def __init__(self, t, leaf=False):
        """Initialize a B*-Tree Node"""
        self.t = t
        self.leaf = leaf
        self.children = []
        self.keys = []

class BStarTree:
    def __init__(self, t):
        """Initialize a B*-Tree with a minimum degree 't' """
        self.root = BStarTreeNode(t, True)
        self.t = t

    def traverse(self, node=None):
        """Print the B*-Tree in an inorder traversal format"""
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")

        if not node.leaf:
            self.traverse(node.children[len(node.keys)])



    def search(self, key, node=None):
        """Search for a key in the B*-Tree"""
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            return node
        
        if node.leaf:
            return None
        
        return self.search(key, node.children[i])

    def insert(self, key):
        """Insert a key into the B*-Tree"""
        root = self.root

        if len(root.keys) == (2 * self.t) - 1:
            new_root = BStarTreeNode(self.t, False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        
        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        """Insert a key into a non-full node"""
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(key)
            node.keys.sort()
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
                self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        """Split a full child node and promote the middle key"""
        t = self.t
        full_child = parent.children[index]
        new_child = BStarTreeNode(t, full_child.leaf)

        # B*-Tree Optimization
        redistribute_count = (2 * t -1) // 3
        new_child.keys = full_child.keys[-redistribute_count:]
        full_child.keys = full_child.keys[:-redistribute_count]

        parent.keys.insert(index, full_child.keys.pop(-1))
        parent.children.insert(index + 1, new_child)

        if not full_child.leaf:
            new_child.children = full_child.children[-redistribute_count:]
            full_child.children = full_child.children[:-redistribute_count]




# B*-Tree of order 3
BStar = BStarTree(t=3)
values = [10, 20, 5, 6, 12, 30, 7, 17, 25, 40, 50, 60]

for v in values:
    BStar.insert(v)

print("B*-Tree Inorder Traversal (Sorted Order):")
BStar.traverse()
print("\n")

key_to_search = 25
result = BStar.search(key_to_search)
if result:
    print(f"Key {key_to_search} found in the B*-Tree")
else:
    print(f"Key {key_to_search} not found in the B*-Tree")


# B*-Tree Inorder Traversal (Sorted Order):
# 5 6 10 12 20 

# Key 25 not found in the B*-Tree