# Depth first search (DFS) implementation in Python

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Process the node (e.g., print it)
    
    for neighbor in graph[start]:
        print(f"Checking neighbor: {neighbor} of node: {start}")
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')  # Output: A B D E F C (or any other order depending on the graph structure)