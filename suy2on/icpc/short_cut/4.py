##지름길
import heapq
import sys
import collections

input = sys.stdin.readline
paths = collections.defaultdict(list)

N, distance = map(int, input().split())
for _ in range(N):
    head, tail, dis = map(int, input().split())
    paths[head].append([tail, dis])


pq = []
heapq.heappush(pq, [0,0])
costs = [float('inf')] * (distance+1)
costs[0] = 0

while pq:
    cost, node = heapq.heappop(pq)

    for n, c in paths[node]:
        if n <= distance and costs[n] > cost + c:
            costs[n] = cost + c
            heapq.heappush(pq, [cost+c, n])

    if node+1 <= distance and costs[node+1] > cost + 1:
        costs[node+1] = cost + 1
        heapq.heappush(pq, [cost + 1, node+1])


print(costs[distance])