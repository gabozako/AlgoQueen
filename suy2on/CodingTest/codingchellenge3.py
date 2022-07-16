# 총합이 0이 아니면 -> -1
# 총합이 0이면 가능
import sys
import collections

sys.setrecursionlimit(300000)

answer = 0


def solution(a, edges):
    if sum(a) != 0:
        return -1

    visited = [0] * len(a)
    paths = collections.defaultdict(list)

    for edge in edges:
        paths[edge[0]].append(edge[1])
        paths[edge[1]].append(edge[0])

    def dfs(node):
        global answer

        for next_ in paths[node]:
            if not visited[next_]:
                visited[next_] = 1
                a[node] += dfs(next_)

        answer += abs(a[node])
        return a[node]

    visited[0] = 1
    dfs(0)

    return answer