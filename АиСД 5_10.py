import sys


class Node:
    __slots__ = ('data', 'count', 'left', 'right')

    def __init__(self, key):
        self.data = key
        self.count = 1
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
                current.count += 1
                return

    def inorder_traversal(self):
        result = []
        stack = []
        current = self.root

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append((current.data, current.count))
                current = current.right

        return result
data = sys.stdin.read().split()
bst = BinarySearchTree()

for s in data:
    num = int(s)
    if num == 0:
        break
    bst.insert(num)

for data, count in bst.inorder_traversal():
    print(f"{data} {count}")