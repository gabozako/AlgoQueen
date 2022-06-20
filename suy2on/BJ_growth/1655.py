import heapq
import sys

input = sys.stdin.readline
leftPQ = [] # 내림차순 : 최대힙
rightPQ = [] # 오름차순 : 최소힙


N = int(input())
heapq.heappush(leftPQ, -int(input()))
print(-leftPQ[0])

for _ in range(N-1):
    mid = -leftPQ[0]
    num = int(input())

    if mid >= num: # 작으면
        heapq.heappush(leftPQ, -num)
    else: # 크면
        heapq.heappush(rightPQ, num)

    # leftPQ의 root가 답이 되도록 밸런스 맞추기
    if len(leftPQ) - len(rightPQ) > 1 :
        heapq.heappush(rightPQ, -heapq.heappop(leftPQ))

    elif len(leftPQ) < len(rightPQ) :
        heapq.heappush(leftPQ, -heapq.heappop(rightPQ))

    print(-leftPQ[0])




