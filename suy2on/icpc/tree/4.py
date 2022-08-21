## 단지수
import sys
import collections
input = sys.stdin.readline

dxy = [[0,1], [0,-1], [1,0], [-1,0]]
N = int(input())
houses = []

def is_valid(x,y):
    if 0 <= x <= N-1 and 0 <= y <= N-1 and houses[x][y] == "1":
        return True
    return False


for _ in range(N):
    houses.append(input().rstrip())

visited = [[False] * N for _ in range(N)]

def bfs(start):
    queue = collections.deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    home = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if is_valid(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                home += 1
                queue.append([nx,ny])

    return home




answer = 0
howMany = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and houses[i][j] == "1":
            howMany.append(bfs([i,j]))
            answer += 1

print(answer)
howMany.sort()
print("\n".join(map(str, howMany)))