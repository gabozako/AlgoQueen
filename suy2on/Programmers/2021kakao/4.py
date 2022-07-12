import heapq
import collections


def solution(n, s, a, b, fares):
    costs = [[float('inf')] * (n + 1) for i in range(n + 1)]  # 각 노드마다 최단거리 기록
    paths = collections.defaultdict(list)
    answer = float('inf')

    def bfs(start):
        queue = []
        heapq.heappush(queue, [start, 0])
        costs[start][start] = 0

        # bfs 자식 넣어줄때 다 넣어주고 비교 -> 비교해주면서 넣어주기로 바꿨을 뿐인데 시간 차이 꽤 났다
        while queue:
            node, dis = heapq.heappop(queue)
            for nnode, d in paths[node]:
                if costs[start][nnode] > dis + d:
                    costs[start][nnode] = dis + d
                    heapq.heappush(queue, [nnode, dis + d])

    # 루트기록
    for fare in fares:
        paths[fare[0]].append([fare[1], fare[2]])
        paths[fare[1]].append([fare[0], fare[2]])

    for i in range(n):
        bfs(i + 1)

    for mid in range(1, n + 1):
        answer = min(answer, costs[s][mid] + costs[mid][a] + costs[mid][b])

    return answer