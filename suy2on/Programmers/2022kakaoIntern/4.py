import heapq
import collections


# 산 봉우리에서 각각 게이트까지의 최소 intense를 갖는 길을 찾고 최소 갱신
def solution(n, paths, gates, summits):
    answer = {s: float("inf") for s in summits}
    routes = collections.defaultdict(list)
    gates = set(gates)
    summits = set(summits)

    for path in paths:
        routes[path[0]].append([path[1], path[2]])
        routes[path[1]].append([path[0], path[2]])

    pq = []
    costs = [float('inf')] * (n + 1)
    # summit을 쫙 넣어주고 각자의 최단거리를 찾아간다 : 이때 중간에 다른 경로에 먹혀도 괜찮다
    for summit in summits:
        heapq.heappush(pq, [0, summit, summit])
        costs[summit] = 0

    while pq:
        c, node, summit = heapq.heappop(pq)

        # 다음 갈 곳
        for route in routes[node]:
            nnode, ins = route
            # 출입구면 : 최단거리 체크 안해줌 (뒤에온 더 작은 summit이 같은 거리일 수 있어서)
            if nnode in gates:
                answer[summit] = min(answer[summit], max(ins, c))
                continue
            # 쉼터면
            elif nnode not in summits and costs[nnode] > max(ins, c):
                costs[nnode] = max(ins, c)
                heapq.heappush(pq, [max(ins, c), nnode, summit])

    return sorted(answer.items(), key=lambda x: (x[1], x[0]))[0]