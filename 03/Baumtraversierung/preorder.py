class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node is None:
        return
    print(node.value)  # Besuche den aktuellen Knoten
    preorder_traversal(node.left)  # Traversiere den linken Teilbaum
    preorder_traversal(node.right)  # Traversiere den rechten Teilbaum


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

# Preorder-Traversierung aufrufen
preorder_traversal(root)
