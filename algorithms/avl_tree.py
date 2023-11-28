#!/Users/neevekadosh/anaconda3/bin/python3
'''
AVL Tree's max difference in height is max 1 between 
nodes in left and right tree.
Run time: O(log(n))
'''

class Node:
    # Constructor 
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# AVL Tree class
class AVLTree:
    def insert(self, root, key):
        # Step 1 - normal BST
        if not root:
            return Node(key)
        elif key <  root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Step 2 - Update ancestor node height
        root.height = 1 + max(
            self.get_height(root.left),
            self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
        
        # Step 4 - Cases
        # 1. Left left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # 2. Right right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
            
        # 3. Left right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # 4. Right left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    
    def left_rotate(self, z):
        y = z.right
        t2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = t2
        
        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        
        return y
        
    def right_rotate(self, z):
        y = z.left
        t3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = t3
        
        # Update height
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        
        return y
            
            
    def get_height(self, root):
        if root is None:
            return 0
        
        return root.height
    
    
    def get_balance(self, root):
        if root is None:
            return 0
        
        return self.get_height(root.left) - \
            self.get_height(root.right)
    
    def pre_order(self, root):
        '''root->left->right'''
        if root is None:
            return
        
        print("{0} ".format(root.key))
        self.pre_order(root.left)
        self.pre_order(root.right)


    def in_order(self, root):
        '''left->root->right'''
        if root is None:
            return
        
        self.in_order(root.left)
        print(root.key)
        self.in_order(root.right)
    
    def post_order(self, root):
        '''left->right->root'''
        if root is None:
            return
        
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.key)
        
if __name__ == "__main__":
    print("AVL Tree Startup")
    avl_tree = AVLTree() 
    root = None
    
    root = avl_tree.insert(root, 10) 
    root = avl_tree.insert(root, 20) 
    root = avl_tree.insert(root, 30) 
    root = avl_tree.insert(root, 40) 
    root = avl_tree.insert(root, 50) 
    root = avl_tree.insert(root, 25) 

    avl_tree.post_order(root)
