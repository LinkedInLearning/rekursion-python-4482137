class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return []
    else:
        result = []
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
        return result

# Beispielbaum
#       1
#      / \
#     2   3
#    / \
#   4   5

# Beispielbaum erstellen
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Inorder-Traversierung durchführen
result = inorder_traversal(root)
print(result)  # Ausgabe: [4, 2, 5, 1, 3]
