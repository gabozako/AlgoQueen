import collections


## 블럭이동하기
def solution(board):
    N = len(board)
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def is_valid(r, c):
        if 1 <= r <= N and 1 <= c <= N and board[r-1][c-1] == 0:
            return True

        return False


    queue = collections.deque()
    queue.append((0, ((1, 1), (1, 2))))
    visited = set()
    visited.add(((1, 1), (1, 2)))

    while queue:
        cost, pos = queue.popleft()
        p1, p2 = pos

        if p1 == (N,N) or p2 == (N,N):
            return cost

        # 동서남북
        for i in range(4):
            np1x = p1[0] + dxy[i][0]
            np1y = p1[1] + dxy[i][1]

            np2x = p2[0] + dxy[i][0]
            np2y = p2[1] + dxy[i][1]

            if is_valid(np1x, np1y) and is_valid(np2x, np2y):
                if ((np1x, np1y), (np2x, np2y)) not in visited:
                    queue.append([cost + 1, ((np1x, np1y), (np2x, np2y))])
                    visited.add(((np1x, np1y), (np2x, np2y)))

        # 회전 : 가로일때
        if p1[0] == p2[0]:
            for d in [-1,1]: # 위, 아래
                if is_valid(p1[0] + d, p1[1]) and is_valid(p2[0] + d, p2[1]):
                    if d == -1:
                        for p in [p1, p2]:
                            if (p, (p[0] + d, p[1])) not in visited:
                                queue.append([cost + 1, (p, (p[0] + d, p[1]))])
                                visited.add((p, (p[0] + d, p[1])))
                    else:
                        for p in [p1, p2]:
                            if ((p[0] + d, p[1]), p) not in visited:
                                queue.append([cost + 1, ((p[0] + d, p[1]), p)])
                                visited.add(((p[0] + d, p[1]), p))

        else:  # 회전 : 세로일 때
            for d in [-1,1]: # 왼, 오른쪽
                if is_valid(p1[0], p1[1] + d) and is_valid(p2[0], p2[1] + d):
                    if d == -1:
                        for p in [p1,p2]:
                            if (p, (p[0], p[1]+d)) not in visited:
                                queue.append([cost + 1, (p, (p[0], p[1]+d))])
                                visited.add((p, (p[0], p[1]+d)))
                    else:
                        for p in [p1,p2]:
                            if ((p[0], p[1] + d), p) not in visited:
                                queue.append([cost + 1,((p[0], p[1] + d), p)])
                                visited.add(((p[0], p[1] + d), p))




print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))


