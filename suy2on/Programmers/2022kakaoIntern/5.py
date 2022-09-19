import collections


def solution(rc, operations):
    R = len(rc)
    C = len(rc[0])

    def shift_row():
        queue = collections.deque()
        for c in range(C):
            queue.append(rc[0][c])
            for r in range(R - 1):
                queue.append(rc[r + 1][c])
                rc[r + 1][c] = queue.popleft()
            rc[0][c] = queue.popleft()

    def rotate():
        queue = collections.deque()
        queue.append(rc[0][0])

        # 시계방향으로 밀기
        for c in range(C - 1):
            queue.append(rc[0][c + 1])
            rc[0][c + 1] = queue.popleft()

        for r in range(R - 1):
            queue.append(rc[r + 1][C - 1])
            rc[r + 1][C - 1] = queue.popleft()

        for c in range(C - 1, 0, -1):
            queue.append(rc[R - 1][c - 1])
            rc[R - 1][c - 1] = queue.popleft()
        for r in range(R - 1, 0, -1):
            queue.append(rc[r - 1][0])
            rc[r - 1][0] = queue.popleft()

    for op in operations:
        if op == "Rotate":
            rotate()
        else:
            shift_row()
    return rc