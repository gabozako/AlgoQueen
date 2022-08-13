## 연결요소
import sys
import collections
input = sys.stdin.readline

N, line = map(int, input().split())
paths = collections.defaultdict(list)

for _ in range(line):
    node1, node2 = map(int, input().split())
    paths[node1].append(node2)
    paths[node2].append(node1)

visited = [False] * (N+1)
def bfs(start):
    queue = collections.deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for nn in paths[node]:
            if not visited[nn]:
                visited[nn] = True
                queue.append(nn)

answer = 0

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)