import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
positions = [0] * (N+1)
distances = [[0] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    positions[i] = list(map(int, input().split()))

# for i in range(1,N):
#     for j in range(i+1,N+1):
#         dis = min(abs(positions[i][0] - positions[j][0]), abs(positions[i][1] - positions[j][1]))
#         if (positions[i][2] + positions[j][2]) % K == 0:
#             dis = min(dis, positions[i][2] + positions[j][2])
#         distances[i][j] = dis
#         distances[j][i] = dis

def distance(i,j):
    dis = min(abs(positions[i][0] - positions[j][0]), abs(positions[i][1] - positions[j][1]))
    if (positions[i][2] + positions[j][2]) % K == 0:
        dis = min(dis, positions[i][2] + positions[j][2])
    return dis


pq = []
heapq.heappush(pq, [0, 1])
costs = [float('inf')] * (N+1)
costs[1] = 0

while pq:
    cost, node = heapq.heappop(pq)
    for i in range(1, N+1):
        if distance(node, i) + cost < costs[i]:
            costs[i] = distance(node,i) + cost
            heapq.heappush(pq, [distance(node,i) + cost, i])


for i in range(1,N+1):
    print(costs[i])


