class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end=" ")

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

# Postorder-Traversierung des Baums
print("Postorder-Traversierung:")
postorder_traversal(root)
