#!/Users/neevekadosh/anaconda3/bin/python3

'''
Run Time: O(log(n))
Rules:
- root is black
- leaves are black (null children of nodes)
- children of red node are black
- all have same black depth
- Every node is colored red or black
- Every path from a node to leaves has same 
 number of black nodes
- No two adjacent red nodes, no red parent or child

Red Black Tree better for Insert / Delete
AVL Tree better for Search
'''