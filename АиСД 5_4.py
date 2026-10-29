class Node:
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
        else:
            cur_node = self.root
            while True:
                if key < cur_node.data:
                    if cur_node.left is None:
                        cur_node.left = Node(key)
                        break
                    cur_node = cur_node.left
                elif key > cur_node.data:
                    if cur_node.right is None:
                        cur_node.right = Node(key)
                        break
                    cur_node = cur_node.right
                else:
                    break

    def find_second_max(self):
        if self.root is None:
            return None

        # Ищем максимальный элемент (самый правый)
        parent = None
        current = self.root
        while current.right is not None:
            parent = current
            current = current.right

        # Если у максимального есть левое поддерево, ищем в нем максимум
        if current.left is not None:
            current = current.left
            while current.right is not None:
                current = current.right
            return current.data
        else:
            # Если левого поддерева нет, возвращаем родителя
            return parent.data

bst = BinarySearchTree()
numbers = list(map(int, input().split()))
for num in numbers:
    if num == 0:
        break
    bst.insert(num)

print(bst.find_second_max())