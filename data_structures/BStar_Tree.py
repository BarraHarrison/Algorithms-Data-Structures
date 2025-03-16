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
        pass