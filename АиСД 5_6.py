import sys


class Node:
    __slots__ = ('data', 'left', 'right')

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return

    def get_leaves_sorted(self):
        if not self.root:
            return []

        leaves = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        leaves.sort()
        return leaves

bst = BinarySearchTree()
data = sys.stdin.read().split()

for s in data:
    num = int(s)
    if num == 0:
        break
    bst.insert(num)

leaves = bst.get_leaves_sorted()
print('\n'.join(map(str, leaves)))