class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_height(node):
    if node is None:
        return 0
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    return max(left_height, right_height) + 1

def print_level(node, level):
    if node is None:
        return
    if level == 1:
        print(node.value, end=" ")
    elif level > 1:
        print_level(node.left, level-1)
        print_level(node.right, level-1)

def levelorder_traversal(node):
    height = get_height(node)
    for level in range(1, height+1):
        print_level(node, level)

# Beispielbaum
#       1
#      / \
#     2   3
#    / \
#   4   5

# Erstellen des Beispielbaums
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Levelorder-Traversierung des Baums
print("Levelorder-Traversierung:")
levelorder_traversal(root)
