graph={
    1:[2,3],
    2:[1,4,5],
    3:[1,6,7],
    4:[2,8],
    5:[2,8],
    6:[3,8],
    7:[3,8],
    8:[4,5,6,7]
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
dfs(visited, graph, 1,8)
