class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = Graph(4)
G3 = Graph(4)
G_self = Graph(4)

# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1  # AB, AC, AD
G1.graph[1][0] = 1; G1.graph[1][2] = 1 # BA, BC
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1 #CA, CB, CD
G1.graph[3][0] = 1; G1.graph[3][2] = 1 # DA, DC

print("G1 Undirected Graph")
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()

print()

# 0 == A, 1 == B, 2 == C, 3 == D
G3.graph[0][1] = 1; G3.graph[0][2] = 1 # BA, BC
G3.graph[3][0] = 1; G3.graph[3][2] = 1 # DA, DC

print("G3 Directed Graph")
for row in range(G3.SIZE):
    for col in range(G3.SIZE):
        print(G3.graph[row][col], end=' ')
    print()

print()

# 0 == A, 1 == B, 2 == C, 3 == D
G_self.graph[0][3] = 1 # AC
G_self.graph[1][2] = 1; G_self.graph[1][3] = 1 # BC, BD
G_self.graph[2][1] = 1 # CB
G_self.graph[3][0] = 1; G_self.graph[3][1] = 1 # DA, DB

print("G_self Undirected Graph")
for row in range(G_self.SIZE):
    for col in range(G_self.SIZE):
        print(G_self.graph[row][col], end=' ')
    print()