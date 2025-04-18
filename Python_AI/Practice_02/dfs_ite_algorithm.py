def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        current_node = stack.pop()

        if current_node == goal:
            return True
        
        if current_node not in visited:
            visited.add(current_node)
            print(f"Visiting node: {current_node}")

        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

graph = {
    'A': ['B'],
    'B': ['C', 'D', 'E'],
    'E': ['F']
}

if dfs(graph, 'A', 'F'):
    print("Goal reached")
else:
    print("Goal not found")