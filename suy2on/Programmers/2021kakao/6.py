import collections
import itertools


def solution(board, r, c):
    cardNums = collections.defaultdict(list)
    idx = 1
    drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    answer = float('inf')

    # 카드들 위치 체크
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cardNums[board[i][j]].append([i, j])
                idx += 1

    def is_valid(i, j):
        if 0 <= i <= 3 and 0 <= j <= 3:
            return True
        else:
            return False

    def bfs(start, finish, b):
        queue = collections.deque()
        queue.append([start, 0])
        visited = [[0] * 4 for _ in range(4)]
        visited[start[0]][start[1]] = 1

        while queue:
            pos, cost = queue.popleft()
            # 방문
            if pos == finish:
                return cost

            # 한칸씩
            for i in range(4):
                nr = pos[0] + drc[i][0]
                nc = pos[1] + drc[i][1]
                if is_valid(nr, nc) and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append([[nr, nc], cost + 1])
            # CTRL
            for i in range(4):
                for j in range(4):
                    nr = pos[0] + drc[i][0] * j
                    nc = pos[1] + drc[i][1] * j
                    # 끝에도달
                    if not is_valid(nr, nc):
                        visited[nr][nc] = 1
                        queue.append([nr - drc[i][0], nc - drc[i][1], cost + 1])
                        break
                    # 카드발견
                    if b[nr][nc]:
                        visited[nr][nc] = 1
                        queue.append([[nr, nc], cost + 1])
                        break

    for combi in itertools.permutations(cardNums.keys()):

        q = collections.deque()
        q.append([[r, c], 0, 0])

        while q:
            cur, i, cost = q.popleft()
            bfs(combi[0]



