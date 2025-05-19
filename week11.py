from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited):
    queue = deque()
    visited[i] = 1
    queue.append(i)

    while queue:
        j = queue.popleft()
        for k in range(len(graph)):
            if g[j][k] == 1 and not visited[k]:
                visited[k] = 1
                queue.append(k)
        print(chr(ord('A') + j), end=' ')



visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]

dfs(graph, 6, visited_dfs)
print()
bfs(graph, 6, visited_bfs)