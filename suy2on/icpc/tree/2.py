## DFS와 BFS
import sys
import collections
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

paths = collections.defaultdict(list)
N, line, start = map(int, input().split())


lines = []
for _ in range(line):
    node1, node2 = (map(int, input().split()))
    paths[node1].append(node2)
    paths[node2].append(node1)


def bfs():
    queue = collections.deque()
    visited = [False] * (N+1)

    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for nn in sorted(paths[node]): # 매번정렬
            if not visited[nn]:
                visited[nn] = True
                queue.append(nn)

visited = [False] * (N+1)
def dfs(node):
    visited[node] = True
    print(node, end=" ")
    for nn in sorted(paths[node]): # 매번정렬
        if not visited[nn]:
            dfs(nn)



dfs(start)
print()
bfs()




