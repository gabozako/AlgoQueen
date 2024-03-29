import collections


# 다익스트라
# 중복체크 -> 카드의 상태
# 상하좌우, CRTL + 상하좌우, Enter -> 9개
# 카드가 다 없어진 상태의 처음 키조작횟수 
def solution(board, r, c):
    drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def is_valid(x, y):
        if 0 <= x <= 3 and 0 <= y <= 3:
            return True
        return False

    # 카드기록
    cards = []
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                cards.append([i, j])

    # 최소조작횟수
    q = collections.deque()
    q.append([0, r, c, (1 << len(cards)) - 1, 0])
    # 카드유무/선택유무/r/c
    visited = [[[[False] * 4 for _ in range(4)] for _ in range((1 << len(cards)))] for _ in
               range((1 << len(cards)))]
    # 모든카드가 있고/ 선택되지 않았고
    visited[(1 << len(cards)) - 1][0][r][c] = True

    while q:
        print(q)
        cost, rr, cc, card, select = q.popleft()

        if card == 0:
            return cost

        # 상하좌우
        for i in range(4):
            nr = rr + drc[i][0]
            nc = cc + drc[i][1]
            if is_valid(nr, nc) and not visited[card][select][nr][nc]:
                visited[card][select][nr][nc] = True
                q.append([cost + 1, nr, nc, card, select])

        # CTRL + 상하좌우
        for i in range(4):
            nr = rr
            nc = cc
            # 가능한 곳 까지 이동
            while is_valid(nr + drc[i][0], nc + drc[i][1]):
                nr = nr + drc[i][0]
                nc = nc + drc[i][1]
                if [nr, nc] in cards and card & 1 << cards.index([nr, nc]):
                    break

            if not visited[card][select][nr][nc]:
                visited[card][select][nr][nc] = True
                q.append([cost + 1, nr, nc, card, select])

        # Enter
        if [rr, cc] in cards and card & 1 << cards.index([rr, cc]) and not select & 1 << cards.index([rr, cc]):
            # 카드선택된 것이 없다면
            if not select:
                select ^= 1 << cards.index([rr, cc])
            # 카드 선택된 것이 있다면
            else:
                c = board[cards[int(select**(1/2))][0]][cards[int(select**(1/2))][1]]
                # 같은 카드면 카드 빼기
                if c == board[rr][cc]:
                    card ^= 1 << int(select ** (1/2))
                    card ^= 1 << cards.index([rr, cc])

                select = 0

            if not visited[card][select][rr][cc]:
                visited[card][select][rr][cc] = True
                q.append([cost + 1, rr, cc, card, select])

print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]],0,1))