import heapq

# INFORMED SEARCH: Greedy Best-First Search
def greedy_search(graph, heuristic, start, goal):
    # Priority Queue berisi tuple: (nilai_heuristic, node_saat_ini, jalur)
    pq = [(heuristic[start], start, [start])]
    visited = set()
    
    while pq:
        h, node, path = heapq.heappop(pq)
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, new_path))
    return None