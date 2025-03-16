# B-Trees are self-balancing designed to store large amounts of data
# Unlike BST, B-Trees can have multiple children per node

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        """Initialize a B-Tree with minimum degree 't' (order t)"""
        self.root = BTreeNode(leaf=True)
        self.t = t

    def traverse(self, node=None):
        """Print the B-Tree inorder traversal format"""
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if not node.leaf:
                self.traverse(node.children[i])
            print(node.keys[i], end=" ")

        if not node.leaf:
            self.traverse(node.children[len(node.keys)])

    def search(self, key, node=None):
        """Search for a key in the B-Tree"""
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
        """Insert a key into the B-Tree"""
        root = self.root

        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        """Insert a key into a non-full node"""
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
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
        new_child = BTreeNode(leaf=full_child.leaf)

        parent.keys.insert(index, full_child.keys[t - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = full_child.keys[t:(2 * t)]
        full_child.children = full_child.children[0:t]


