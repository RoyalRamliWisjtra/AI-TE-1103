from collections import deque

# UNINFORMED SEARCH: Breadth-First Search (BFS)
def bfs_search(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None