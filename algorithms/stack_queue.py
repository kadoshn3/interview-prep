#!/Users/neevekadosh/anaconda3/bin/python3

from collections import deque

# Stack Last in First out
print("Stack Example...")
stack = deque(['Porche', 'Honda', 'Ferrari', 'Ford'])

print(stack)
stack.append('Hyundai')
print(stack)
while stack:
    print(stack.pop())

# Queue First in First out
print("\nQueue Example...")
queue = deque(['Porche', 'Honda', 'Ferrari', 'Ford'])
print(queue)
queue.append('Audi')
print(queue)
while queue:
    print(queue.popleft())
