import sys


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        """Добавление элемента в дерево"""
        if self.root is None:
            self.root = Node(key)
            return True

        current = self.root
        while current is not None:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    return True
                current = current.left
            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    return True
                current = current.right
            else:
                return False  # Элемент уже существует
        return False

    def search(self, key):
        """Поиск элемента в дереве"""
        current = self.root
        while current is not None:
            if key < current.data:
                current = current.left
            elif key > current.data:
                current = current.right
            else:
                return True
        return False

    def delete(self, key):
        """Удаление элемента из дерева"""
        if self.root is None:
            return False

        # Поиск узла для удаления и его родителя
        current = self.root
        parent = None
        is_left_child = False

        while current is not None and current.data != key:
            parent = current
            if key < current.data:
                current = current.left
                is_left_child = True
            else:
                current = current.right
                is_left_child = False

        if current is None:
            return False  # Элемент не найден

        # Случай 1: Узел без потомков
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None

        # Случай 2: Узел с одним потомком
        elif current.right is None:  # Только левый потомок
            if current == self.root:
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left

        elif current.left is None:  # Только правый потомок
            if current == self.root:
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right

        # Случай 3: Узел с двумя потомками
        else:
            # Находим максимальный элемент в левом поддереве (как требуется в задаче)
            max_node = current.left
            max_parent = current
            is_max_left = True

            while max_node.right is not None:
                max_parent = max_node
                max_node = max_node.right
                is_max_left = False

            # Заменяем значение текущего узла на максимальное из левого поддерева
            current.data = max_node.data

            # Удаляем узел с максимальным значением
            if is_max_left:
                max_parent.left = max_node.left
            else:
                max_parent.right = max_node.left

        return True

    def print_tree(self, node=None, level=0):
        """Печать дерева в заданном формате (симметричный обход LNR)"""
        if node is None:
            node = self.root

        if node.left is not None:
            self.print_tree(node.left, level + 1)

        print("." * level + str(node.data))

        if node.right is not None:
            self.print_tree(node.right, level + 1)

tree = BinarySearchTree()

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split()
    command = parts[0]

    if command == "ADD":
        n = int(parts[1])
        if tree.add(n):
            print("DONE")
        else:
            print("ALREADY")

    elif command == "DELETE":
        n = int(parts[1])
        if tree.delete(n):
            print("DONE")
        else:
            print("CANNOT")

    elif command == "SEARCH":
        n = int(parts[1])
        if tree.search(n):
            print("YES")
        else:
            print("NO")

    elif command == "PRINTTREE":
        tree.print_tree()