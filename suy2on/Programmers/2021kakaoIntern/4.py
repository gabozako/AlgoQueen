import heapq
import collections

def solution(n, start, end, roads, traps):
    answer = 0
    paths = collections.defaultdict(list)

    def is_switch(node, nnode, ts):
        cnt = 0
        if node in traps:
            traps.index(node)
            cnt += ts.count(str(node))
        if nnode in traps:
            cnt += ts.count(str(nnode))

        return cnt % 2 == 1

    # 활성화를 True, False로
    for p, q, s in roads:
        paths[p].append([q,True,s])
        paths[q].append([p,False,s])

    # trap의 어느상태로 여기를 방문했는지
    costs = [[0] * (1 << 9) for _ in range(n)]

    pq = [[0, start, 0]]
    costs[0][start] = 0

    while pq:
        cost, node, ts = heapq.heappop(pq)

        for path in paths[node]:
            nnode, valid, c = path

            # 바뀌었으면 valid 하지 않은게 활성화
            if is_switch(node, nnode, ts) and not valid:
                if costs[nnode][ts] > cost + c:
                    costs[nnode][ts] = cost + c
                    if nnode in traps:
                        heapq.heappush(pq, [cost + c, nnode, ts ^ (1 << traps.index(nnode))])
                    else:
                        heapq.heappush(pq, [cost + c, nnode, ts])

            # 바뀌지 않았으면 valid 한쪽이 활성화
            elif not is_switch(node, nnode, ts) and valid:
                if costs[nnode][ts] > cost + c:
                    costs[nnode][ts] = cost + c
                    if nnode in traps:
                        heapq.heappush(pq, [cost + c, nnode, ts ^ (1 << traps.index(nnode))])
                    else:
                        heapq.heappush(pq, [cost + c, nnode, ts])



    return min(costs[end].values())

print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))