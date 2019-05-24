from btnode import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_root(self, item):
        self.root = Node(item)

    @staticmethod
    def add_right(node, item):
        node.right = Node(item)

    @staticmethod
    def add_left(node, item):
        node.left = Node(item)

    def __str__(self):
        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        lst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lst.append(node.data)
                recurse(node.right)

        recurse(node)
        return iter(lst)

if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_root(1)
    tree.add_right(tree.root, 2)
    tree.add_left(tree.root, 3)
    tree.add_left(tree.root.left, 4)
    tree.add_right(tree.root.left, 5)
    print(tree)
    for i in tree.inorder():
        print(i)



