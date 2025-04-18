def dfs_recursive(graph, start, goal, visited, parent=None):
    visited.add(start)

    print(f"Visiting node: {start}")

    if start == goal:
        return True
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs_recursive(graph, neighbor, goal, visited, parent):
                return True
            
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['E', 'F'],
    'C': ['G']
}

path = {}
visited = set()
if(dfs_recursive(graph, 'A', 'F', visited)):
    print("Goal reached")
else:
    print("Goal not found")