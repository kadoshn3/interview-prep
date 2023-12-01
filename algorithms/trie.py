#!/Users/neevekadosh/anaconda3/bin/python3

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        # self.children = [None] * 26
        
        # Keep track of number of strings stored in
        # root node to any trie node
        self.word_count = 0

def insert_key(root, key):
    # Initialize current node with root node
    current_node = root
    
    # Iterate each 'character' in the string
    for char in key:
        # Check if the node exists
        if current_node.children[ord(char) - ord('a')] \
            == None:
            # DNE make a new node
            new_node = TrieNode()
            
            # Keep reference for new node
            current_node.children[ord(char) - ord('a')] = new_node
        
        # Move current node to be new child node
        current_node = current_node.children[ord(char) - ord('a')]

    current_node.word_count += 1
    
    

def print_trie(root):
    if root is not None:
        if root.children is not None:
            print_trie(root.children)
            print(root.children)
    else:
        print(root.items())

if __name__ == "__main__":
    root = TrieNode()
    input_str = ["and", "ant", "do", "geek", "dad", "ball"] 
    
    for key in input_str:
        insert_key(root, key)
    
    # print_trie(root)