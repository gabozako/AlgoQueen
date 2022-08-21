import heapq
import sys

input = sys.stdin.readline

pq = []
N = int(input())

for _ in range(N):
    num = int(input())
    if not num:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)

    else:
        heapq.heappush(pq, num)


