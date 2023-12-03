#!/Users/neevekadosh/anaconda3/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        
        current_node = self.head
        position = 0
        
        if position == index:
            self.insert_at_begin(data)
        else:
            while (current_node != None 
                   and position+1 != index):
                position += 1
                current_node = current_node.next
                
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            
            current_node.next = new_node

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def update_node(self, val, index):
        current_node = self.head
        position = 0
        
        if position == index:
            current_node.data = val
        else:
            while (current_node != None
                   and position != index):
                position += 1
                current_node = current_node.next
            
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
    
    def remove_first_node(self):
        if self.head == None:
            return

        self.head = self.head.next
    
    def remove_last_node(self):
        if self.head is None:
            return
        
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        
        current_node.next = None
    
    def remove_at_index(self, index):
        if self.head is None:
            return
        
        current_node = self.head
        position = 0
        
        # If at the head or start of llist
        if position == index:
            self.remove_first_node()
        else:
            # Loop through until find the index
            while (current_node != None 
                   and position+1 != index):
                position += 1
                current_node = current_node.next
            
            if current_node != None:
                current_node.next = \
                    current_node.next.next
            else:
                print('Index not present')
    
    def remove_node(self, data):
        current_node = self.head
        
        while (current_node != None
               and current_node.next.data != data):
            current_node = current_node.next
        
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
    
    def size_llist(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
        return size
    
if __name__ == '__main__':
    llist = LinkedList()
    
    llist.insert_at_begin('a')
    llist.insert_at_begin('b')
    llist.insert_at_begin('d')
    llist.insert_at_begin('a')
    llist.insert_at_begin('g')
    
    llist.insert_at_index(5, 2)
    
    llist.insert_at_end(99)
    llist.insert_at_end(47)
    
    print('Current List')
    llist.print_ll()
    
    llist.update_node('apple', 3)
    
    # Removes 'g'
    llist.remove_first_node()

    # Removes 47
    llist.remove_last_node()
    
    # Remove 3rd index 'b'
    llist.remove_at_index(3)
    
    llist.remove_node('apple')
    
    print('Updates and removals')
    llist.print_ll()
    
    print('Size:', llist.size_llist())