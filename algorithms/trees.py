#!/Users/neevekadosh/anaconda3/bin/python3


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            
        print(self.data)
        
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        # Compare new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        
    def inorder_traversal(self, root):
        '''left->root->right'''
        result = []
        
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.data)
            result += self.inorder_traversal(root.right) 
        
        return result
    
    def preorder_traversal(self, root):
        '''root->left->right'''
        result = []
        
        if root:
            result.append(root.data)
            result += self.preorder_traversal(root.left)
            result += self.preorder_traversal(root.right)
        
        return result
    
    def postorder_traversal(self, root):
        '''left->right->root'''
        result = []
        
        if root:
            result = self.postorder_traversal(root.left)
            result += self.postorder_traversal(root.right)
            result.append(root.data)
        
        return result
        
    
if __name__=='__main__':
    root = Node(10)
    root.insert(6)
    root.insert(4)
    root.insert(14)
    root.insert(12)
    print("Inorder Traversal:", root.inorder_traversal(root))
    print("Preorder Traversal:", root.preorder_traversal(root))
    print("Postorder Traversal:", root.postorder_traversal(root))