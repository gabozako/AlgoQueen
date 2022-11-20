import collections


def solution(rooms):
    visited = [False] * (len(rooms) + 1)

    # 방끼리 연결고리 count
    cluster = 0

    for start in range(len(rooms)):
        if visited[start]:
            continue
        visited[start] = True

        pre = start
        nxt = rooms[start] - 1
        while not visited[nxt]:
            visited[nxt] = True
            pre = nxt
            nxt = rooms[nxt] - 1

        if nxt == start:
            cluster += 1

        elif nxt == pre:
            cluster += 1

    return max(cluster - 1, 1)