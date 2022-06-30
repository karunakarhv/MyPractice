import collections

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neigh in graph[root]:
            print(visited, neigh)
            dfs(visited, graph, neigh)

if __name__ == "__main__":
    #Dictionary
    graph = {'A':['B','C','D'], 'B':['E'], 'C':['D','E'], 'D':[], 'E':[]}
    dfs(visited, graph, 'A')
    #Display all the adjacent nodes
    # Visited Array in set
    # Queue Datastructure