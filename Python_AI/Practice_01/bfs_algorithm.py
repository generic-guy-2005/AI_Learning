from collections import deque

def bfs(graph, start, goal=None):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current_node = queue.popleft()
        print(f"Visiting node: {current_node}")

        if(current_node == goal):
            print("Goal reached")
            return reconstruct_path(parent, start, goal)

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current_node

    return "Goal not found"

def reconstruct_path(parent, start, goal):
    path = []
    current = goal

    while current:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E']
}


print(bfs(graph, 'A', 'E'))