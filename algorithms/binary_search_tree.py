#!/Users/neevekadosh/anaconda3/bin/python3

'''
Run Time: O(h) which is height of the tree
worst case is O(n) for skewed trees.
'''

class Node:
    # Constructor for new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Util function to insert node into BST
def insert(node, key):
    # If the tree is empty return a new node
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    
    return node    


# Search key in BST
def search(root, key):
    if root is None or root.key == key:
        return root
    
    # Key greater than root's key
    if root.key < key:
        return search(root.right, key)
    
    # Key less than root's key
    return search(root.left, key)


# Get depth of a tree
def max_depth(node):
    if node is None:
        return 0
    
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    
    if left_depth > right_depth:
        return left_depth + 1
    
    return right_depth + 1

if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    
    key = 6
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
    
    key = 60
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
    
    print("Tree height is %d" % (max_depth(root)))

