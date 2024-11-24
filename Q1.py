graph={
    1:[2,3],
    2:[4],
    3:[2],
    4:[5,6],
    5:[7,3],
    6:[],
    7:[6]
    }
visited=set()
def dfs(visited, graph, node, goal):
    if node not in visited:
        print(node)
        visited.add(node)
        if node==goal:
            return True
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal):
                return True
    return False
print("Path Found By DFS:")
dfs(visited, graph, 1,7)
