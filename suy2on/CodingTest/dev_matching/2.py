import collections


def solution(maps):
    total_freqs = collections.defaultdict(int)
    chunks = []
    R = len(maps)
    C = len(maps[0])

    dij = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visited = [[False] * C for _ in range(R)]

    def is_valid(i, j):
        if 0 <= i <= R - 1 and 0 <= j <= C - 1 and maps[i][j] != ".":
            return True
        return False

    def collect_chunk(si, sj):
        queue = collections.deque()
        visited[si][sj] = True
        queue.append([si, sj])
        result = [maps[si][sj]]

        while queue:
            ci, cj = queue.popleft()

            for i in range(4):
                ni = ci + dij[i][0]
                nj = cj + dij[i][1]
                if is_valid(ni, nj) and not visited[ni][nj]:
                    visited[ni][nj] = True
                    result.append(maps[ni][nj])
                    queue.append([ni, nj])

        chunks.append(result)

    # 덩어리 모으기
    for i in range(R):
        for j in range(C):
            if maps[i][j] != "." and not visited[i][j]:
                collect_chunk(i, j)

    # 전쟁결과 반영
    for chunk in chunks:
        freqs = dict(collections.Counter(chunk)).items()
        winner, winner_cnt = sorted(freqs, key = lambda x : (x[1],x[0]), reverse = True)[0]
        for ctr, cnt in freqs:
            if cnt < winner_cnt:
                total_freqs[winner] += cnt
            else:
                total_freqs[ctr] += cnt

    return sorted(total_freqs.values(), reverse=True)[0]


print(solution(["XY..", "YX..", "..YX", ".AXY"]))
