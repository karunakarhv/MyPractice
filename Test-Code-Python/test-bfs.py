def bfs(graph, node):
    visited = set()
    queue = [node]
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node)  # Process the node (e.g., print it)
            visited.add(current_node)
            # Add neighbors to the queue
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')  # Output: A B C D E F

# Calculate the minimum number of jumps to reach the node 'F' from node 'A'
def min_jumps(graph, start, target):
    visited = set()
    queue = [(start, 0)]  # (current_node, jumps)
    
    while queue:
        current_node, jumps = queue.pop(0)
        if current_node == target:
            return jumps
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, jumps + 1))
    return -1  # Return -1 if the target is not reachable

# Example usage:
print(min_jumps(graph, 'A', 'F'))  # Output: 2 (A -> C -> F or A -> B -> E -> F is also 2 jumps)