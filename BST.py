class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None:
            print_tree(root.left, level + 1, "L--- ")
        if root.right is not None:
            print_tree(root.right, level + 1, "R--- ")

 
elements = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

 
root = Node(elements[0])

 
for elem in elements[1:]:
    insert(root, elem)

 
print_tree(root)