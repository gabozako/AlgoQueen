# 플로이드 와샬
def solution(n, s, a, b, fares):
    answer = float("inf")
    costs = [[float('inf')] * (n+1) for _ in range(n+1)]

    for c,d,f in fares:
        costs[c][d] = f
        costs[d][c] = f

    for i in range(1, n + 1):
        costs[i][i] = 0


    for i in range(1,n+1):
        for h in range(1,n+1):
            for t in range(1,n+1):
                if costs[h][i] + costs[i][t] < costs[h][t]:
                    costs[h][t] = costs[h][i] + costs[i][t]

    for i in range(n):
        answer = min(answer, costs[s][i + 1] + costs[i + 1][a] + costs[i + 1][b])

    return answer

print((1<<0) // 2)