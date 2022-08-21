## 특정한 최단경로 문제
import heapq
import sys
import collections

input = sys.stdin.readline
paths = collections.defaultdict(list)

N, E = map(int, input().split())
for _ in range(E):
    n1, n2, cost = map(int, input().split())
    paths[n1].append([n2,cost])
    paths[n2].append([n1,cost])
node1, node2 = map(int, input().split())

def short_cut(start, end):
    pq = []
    costs = [float('inf')] * (N+1)
    heapq.heappush(pq, [0,start])
    costs[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        for n, c in paths[node]:
            if cost + c < costs[n]:
                costs[n] = cost + c
                heapq.heappush(pq, [cost+c, n])

    return costs[end]


answer = min(short_cut(1,node1)+ short_cut(node1,node2) + short_cut(node2,N), short_cut(1,node2) +short_cut(node2,node1) + short_cut(node1, N))
if answer == float('inf'):
    print(-1)
else:
    print(answer)






