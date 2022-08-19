import collections


## 블럭이동하기
def solution(board):
    N = len(board)
    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    spin_dxy_ga = [[1, [-1, -1]], [1, [1, -1]], [0, [-1, 1]], [0, [1, 1]]]
    spin_dxy_se = [[0, [1, -1]], [1, [-1, -1]], [0, [-1, 1]], [0, [1, 1]]]

    def is_valid(r, c):
        if 1 <= r <= N and 1 <= c <= N and board[r - 1][c - 1] == 0:
            return True

        return False


    visited = [[[False] * 2 for _ in range(N+1)] for _ in range(N+1)]
    queue = collections.deque()
    queue.append([0, [[1, 1], [1, 2]]])
    visited[1][1][0] = True
    visited[1][2][1] = True

    while queue:
        cost, pos = queue.popleft()
        p1, p2 = pos

        if p1 == [N,N] or p2 == [N,N]:
            return cost

        # 동서남북
        for i in range(4):
            np1x = p1[0] + dxy[i][0]
            np1y = p1[1] + dxy[i][1]

            np2x = p2[0] + dxy[i][0]
            np2y = p2[1] + dxy[i][1]

            if is_valid(np1x, np1y) and is_valid(np2x, np2y):
                if not visited[np1x][np1y][0] or not visited[np2x][np2y][1]:
                    queue.append([cost + 1, [[np1x, np1y], [np2x, np2y]]])
                    visited[np1x][np1y][0] = True
                    visited[np2x][np2y][1] = True

        # 회전 : 가로일때
        if p1[0] == p2[0]:
            for i in range(4):
                if spin_dxy_ga[i][0] == 0:
                    mp1x = p1[0] + spin_dxy_ga[i][1][0]
                    mp1y = p1[1]
                    nnp1x = mp1x
                    nnp1y = mp1y + spin_dxy_ga[i][1][1]

                    if is_valid(nnp1x, nnp1y) and is_valid(mp1x, mp1y):
                        if not visited[min(nnp1x, p2[0])][min(nnp1y, p2[1])][0] or not visited[max(nnp1x, p2[0])][max(nnp1y, p2[1])][1] :
                            queue.append([cost + 1, [[min(nnp1x, p2[0]), min(nnp1y, p2[1])],
                                                           [max(nnp1x, p2[0]), max(nnp1y, p2[1])]]])
                            visited[min(nnp1x, p2[0])][min(nnp1y, p2[1])][0] = True
                            visited[max(nnp1x, p2[0])][max(nnp1y, p2[1])][1] = True




                else:
                    mp2x = p2[0] + spin_dxy_ga[i][1][0]
                    mp2y = p2[1]
                    nnp2x = mp2x
                    nnp2y = mp2y + spin_dxy_ga[i][1][1]

                    if is_valid(nnp2x, nnp2y) and is_valid(mp2x, mp2y):
                        if not visited[min(nnp2x, p1[0])][min(nnp2y, p1[1])][0] or not visited[max(nnp2x, p1[0])][max(nnp2y, p1[1])][1]:
                            queue.append([cost + 1, [[min(nnp2x, p1[0]), min(nnp2y, p1[1])],
                                                           [max(nnp2x, p1[0]), max(nnp2y, p1[1])]]])

                            visited[min(nnp2x, p1[0])][min(nnp2y, p1[1])][0] = True
                            visited[max(nnp2x, p1[0])][max(nnp2y, p1[1])][1] = True


        else:  # 회전 : 세로일 때
            for i in range(4):
                if spin_dxy_se[i][0] == 0:
                    mp1x = p1[0]
                    mp1y = p1[1] + spin_dxy_se[i][1][1]
                    nnp1x = mp1x + spin_dxy_se[i][1][0]
                    nnp1y = mp1y

                    if is_valid(nnp1x, nnp1y) and is_valid(mp1x, mp1y):
                        if not visited[min(nnp1x, p2[0])][min(nnp1y, p2[1])][0] or not visited[max(nnp1x, p2[0])][max(nnp1y, p2[1])][1] :
                            queue.append([cost + 1, [[min(nnp1x, p2[0]), min(nnp1y, p2[1])],
                                                           [max(nnp1x, p2[0]), max(nnp1y, p2[1])]]])
                            visited[min(nnp1x, p2[0])][min(nnp1y, p2[1])][0] = True
                            visited[max(nnp1x, p2[0])][max(nnp1y, p2[1])][1] = True



                else:
                    mp2x = p2[0]
                    mp2y = p2[1] + spin_dxy_se[i][1][1]
                    nnp2x = mp2x + spin_dxy_se[i][1][0]
                    nnp2y = mp2y

                    if is_valid(nnp2x, nnp2y) and is_valid(mp2x, mp2y):
                        if not visited[min(nnp2x, p1[0])][min(nnp2y, p1[1])][0] or not visited[max(nnp2x, p1[0])][max(nnp2y, p1[1])][1] :
                            queue.append([cost + 1, [[min(nnp2x, p1[0]), min(nnp2y, p1[1])],
                                                           [max(nnp2x, p1[0]), max(nnp2y, p1[1])]]])
                            visited[min(nnp2x, p1[0])][min(nnp2y, p1[1])][0] = True
                            visited[max(nnp2x, p1[0])][max(nnp2y, p1[1])][1] = True


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))


