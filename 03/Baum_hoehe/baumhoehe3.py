class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.middle = None


def get_tree_height(node):
    if node is None:
        return 0
    print(node.value)
    left_height = get_tree_height(node.left)
    right_height = get_tree_height(node.right)
    middle_height = get_tree_height(node.middle)

    return max(left_height, right_height, middle_height) + 1


# Beispielbaum erstellen
root = Node("R")
root.left = Node("L")
root.right = Node("R")
root.middle = Node("M")

root.left.left = Node("LL")
root.left.right = Node("LR")
root.left.left.right = Node("LLR")

# Beispielbaum
#        R
#      / \  \
#     L   M  R
#    / \
#  LL   LR
#  /
# LLR

# Baumhöhe berechnen
height = get_tree_height(root)
print("Baumhöhe:", height)
