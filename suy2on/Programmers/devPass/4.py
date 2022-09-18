import heapq
import collections


def solution(N, fees, dest):
    answer = 0
    paths = collections.defaultdict(list)

    # 수수료기록
    for fee in fees:
        paths[fee[0]].append([fee[1], fee[2]])
        paths[fee[1]].append([fee[0], fee[2]])

    # 다익스트라 : 최소수수료 찾기
    pq = []
    heapq.heappush(pq, [0, 1])
    costs = [float('inf')] * (N + 1)
    costs[1] = 0

    while pq:
        fee, bank = heapq.heappop(pq)

        if bank == dest:
            return fee

        for path in paths[bank]:
            nbank, f = path
            if costs[nbank] > f + fee:
                costs[nbank] = f + fee
                heapq.heappush(pq, [f + fee, nbank])

