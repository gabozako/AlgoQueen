## 서강그라운드
import sys
import heapq
import collections

input = sys.stdin.readline
answer = 0

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
paths = collections.defaultdict(list)

for _ in range(R):
    n1, n2, dis = map(int, input().split())
    paths[n1].append([n2, dis])
    paths[n2].append([n1, dis])

def bfs(start):
    global answer

    pq = []
    heapq.heappush(pq, [0,start])
    costs = [float('inf')] * (N+1)
    costs[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        for n, c in paths[node]:
            if costs[n] > c + cost:
                costs[n] = c + cost
                heapq.heappush(pq, [c+cost, n])
    cnt = 0
    for i in range(1, N+1):
        if costs[i] <= M:
            cnt += items[i-1]

    answer = max(answer, cnt)


for i in range(1, N+1):
    bfs(i)

print(answer)