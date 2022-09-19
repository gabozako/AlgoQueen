import heapq


def solution(alp, cop, problems):
    max_alp = max([p[0] for p in problems])
    max_cop = max([p[1] for p in problems])

    def is_valid(x, y):
        if 0 <= x <= max_alp and 0 <= y <= max_cop:
            return True

        return False

    # 초기값도 잡아줘야함
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    pq = []
    heapq.heappush(pq, [0, alp, cop])
    costs = [[float("inf")] * (max_cop + 1) for _ in range(max_alp + 1)]
    costs[alp][cop] = 0

    while pq:
        time, al, co = heapq.heappop(pq)

        if max_alp <= al and max_cop <= co:
            return time

        if al < max_alp and costs[al + 1][co] > time + 1:
            costs[al + 1][co] = time + 1
            heapq.heappush(pq, [time + 1, al + 1, co])

        if co < max_cop and costs[al][co + 1] > time + 1:
            costs[al][co + 1] = time + 1
            heapq.heappush(pq, [time + 1, al, co + 1])

        # 풀 수 있는 문제 다 풀기
        for problem in problems:
            if problem[0] <= al and problem[1] <= co:
                if costs[min(al + problem[2], max_alp)][min(co + problem[3], max_cop)] > time + problem[4]:
                    costs[min(al + problem[2], max_alp)][min(co + problem[3], max_cop)] = time + problem[4]
                    heapq.heappush(pq,
                                   [time + problem[4], min(al + problem[2], max_alp), min(co + problem[3], max_cop)])
