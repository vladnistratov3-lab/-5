import sys

class Node:
    def __init__(self, key):
        self.key = key
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
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return  # уже есть

    def find_next(self, key):
        current = self.root
        candidate = None
        while current is not None:
            if current.key >= key:
                candidate = current.key
                current = current.left
            else:
                current = current.right
        return candidate if candidate is not None else -1

bst = BinarySearchTree()
n = int(sys.stdin.readline())
prev_query_result = None
output = []
MOD = 10**9

for _ in range(n):
    line = sys.stdin.readline().split()
    op = line[0]
    val = int(line[1])

    if op == '+':
        if prev_query_result is not None:
            val = (val + prev_query_result) % MOD
            prev_query_result = None  # сбрасываем после использования
        bst.insert(val)
    else:  # op == '?'
        result = bst.find_next(val)
        output.append(str(result))
        prev_query_result = result  # запоминаем для возможной следующей операции +

sys.stdout.write("\n".join(output))