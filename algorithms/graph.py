#!/Users/neevekadosh/anaconda3/bin/python3

from collections import deque

def bfs(graph, start, key):
    '''Here the traversal starts from “S” 
    and then it traverses visits all the 
    neighboring vertices — “A”, “B” and “C”. 
    Then it moves to the next vertices.'''
    
    visited = set()
    
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        
        if vertex == key:
            return True
        
        visited.add(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
        
    return False

def dfs(graph, start, key, visited = None):
    '''Here the traversal starts from “S”, 
    then it moves to “A” , from “A” to “D” 
    and finally it reaches the bottom “D”. 
    Then it backtraces from the bottom and 
    visits all the neighboring vertices and 
    moves towards the root.'''
    
    if visited is None:
        visited = set()
    
    if start == key:
        return True

    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, key, visited)
            if found:
                return True

    return False
    
if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
    }
    
    start = 'D'
    key = 'E'
    result = bfs(graph, start, key)
    print(result)
    
    result = dfs(graph, start, key)
    print(result)

    