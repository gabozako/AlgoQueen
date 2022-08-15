## 파티
import sys
import heapq
import collections

input = sys.stdin.readline

N, M, X = map(int, input().split())
paths = collections.defaultdict(list)

for _ in range(M):
    n1, n2, t = map(int, input().split())
    paths[n1].append([n2,t])

## 돌아오는 거리 구하기
costBack = [float('inf')] * (N+1)
pq = []
heapq.heappush(pq, [0,X])
costBack[X] = 0

while pq:
    time, node = heapq.heappop(pq)
    for nn, c in paths[node]:
        if costBack[nn] > c + time:
            costBack[nn] = c + time
            heapq.heappush(pq, [c+time, nn])

## 찾아가는 거리 구하기
def bfs(start):
    costs = [float('inf')] * (N + 1)
    pq = []
    heapq.heappush(pq, [0, start])
    costs[start] = 0

    while pq:
        time, node = heapq.heappop(pq)

        if costs[node] < time:
            continue

        for nn, c in paths[node]:
            if costs[nn] > c + time:
                costs[nn] = c + time
                heapq.heappush(pq, [c + time, nn])

    return costs[X]

answer = 0
for i in range(1, N+1):
    answer = max(answer, bfs(i) + costBack[i])

print(answer)



