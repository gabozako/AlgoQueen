import heapq


def solution(board, r, c):
    cards = {}
    idx = 1
    drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 카드들 위치 체크
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards[(i, j)] = idx
                idx += 1

    def is_valid(i, j):
        if 0 <= i <= 3 and 0 <= j <= 3:
            return True
        else:
            return False

    pq = []
    visited = [[[0] * (1 << (idx - 1)) for _ in range(4)] for _ in range(4)]
    heapq.heappush(pq, (0, [r, c], 0, 0))

    while pq:
        cost, pos, card, target = heapq.heappop()

        # 카드 다 찾은 경우
        if card == 1 << idx - 1:
            return cost

        # 같은 카드찾은 상태로 같은 곳 방문
        if visited[pos[0]][pos[1]][card]:
            continue

        visited[pos[0]][pos[1]][card] = 1

        # 짝 찾은 경우
        if target:
            if board[pos[0]][pos[1]] == target:
                card = card | 1 << cards[(pos[0], pos[1])]
                cost += 1
                target = 0

        # 첫카드 찾은 경우
        else:
            if board[pos[0]][pos[1]]:
                card = card | 1 << cards[(pos[0], pos[1])]
                cost += 1
                target = board[pos[0]][pos[1]]
        # 방향키 4개 하나씩
        for i in range(4):
            nr = pos[0] + drc[i][0]
            nc = pos[1] + drc[i][1]

            if is_valid(nr, nc):
                heapq.heappush(pq, (cost, [nr, nc], card, target))
        # Ctrl 포함
        for i in range(4):
            for _ in range(4):
                nr = pos[0] + drc[i][0]
                nc = pos[1] + drc[i][1]
                if board[nr, nc]:



