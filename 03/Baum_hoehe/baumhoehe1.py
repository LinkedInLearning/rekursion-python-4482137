class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_tree_height(node):
    if node is None:
        return 0
    
    left_height = get_tree_height(node.left)
    right_height = get_tree_height(node.right)
    
    return max(left_height, right_height) + 1

# Beispielbaum erstellen
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# Beispielbaum
#       1
#      / \
#     2   3
#    / \
#   4   5

# Baumhöhe berechnen
height = get_tree_height(root)
print("Baumhöhe:", height)
