import heapq


# 중복체크 -> 카드의 상태, 뒤집은 상태
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
    q = [[0, r, c, (1 << len(cards)) - 1, 0, ""]]
    # 카드유무/선택유무/r/c
    visited = [[[[float(False)] * 4 for _ in range(4)] for _ in range((1 << len(cards)))] for _ in
             range((1 << len(cards)))]
    # 모든카드가 있고/ 선택되지 않았고
    visited[(1 << len(cards)) - 1][0][r][c] = True

    while q:
        cost, rr, cc, card, select, s_card = heapq.heappop(q)

        if card == 0:
            return cost

        # 상하좌우
        for i in range(4):
            nr = rr + drc[i][0]
            nc = cc + drc[i][1]
            if is_valid(nr, nc) and not visited[card][select][nr][nc]:
                visited[card][select][nr][nc] = True
                heapq.heappush(q, [cost + 1, nr, nc, card, select, s_card])

        # CTRL + 상하좌우
        for i in range(4):
            nr = rr
            nc = cc
            # 가능한 곳 까지 이동
            while is_valid(nr + drc[i][0], nc + drc[i][1]):
                nr = nr + drc[i][0]
                nc = nc + drc[i][1]
                if [nr,nc] in cards and card & 1 << cards.index([nr,nc]):
                    break

            if not visited[card][select][nr][nc]:
                visited[card][select][nr][nc] = True
                heapq.heappush(q, [cost + 1, nr, nc, card, select, s_card])

        # Enter
        if [rr, cc] in cards and card & 1 << cards.index([rr, cc]) and not select & 1 << cards.index([rr, cc]):
            # 카드선택
            s_card += str(cards.index([rr,cc]))
            select ^= 1 << cards.index([rr,cc])
            # 두장선택됐으면
            if len(s_card) == 2:
                c1 = board[cards[int(s_card[0])][0]][cards[int(s_card[0])][1]]
                c2 = board[cards[int(s_card[1])][0]][cards[int(s_card[1])][1]]
                # 같은 카드면 카드 빼기
                if c1 == c2:
                    card ^= 1 << int(s_card[0])
                    card ^= 1 << int(s_card[1])
                if card == 0:
                    return cost + 1
                select ^= 1 << int(s_card[0])
                select ^= 1 << int(s_card[1])
                s_card = ""

            if not visited[card][select][rr][cc]:
                visited[card][select][rr][cc] = True
                heapq.heappush(q, [cost + 1, rr, cc, card, select, s_card])