import collections


def solution(beginning, target):
    queue = collections.deque()
    R = len(beginning)
    C = len(beginning[0])
    haveToChange = []

    for r in range(R):
        for c in range(C):
            if beginning[r][c] != target[r][c]:
                haveToChange.append(str(r) + str(c))

    haveToChange.sort()

    # 답인지
    def is_same(changes):
        changes.sort()
        if len(changes) == len(haveToChange):

            for i in range(len(changes)):
                if changes[i] != haveToChange[i]:
                    return False
            return True

        return False

    rows = list(range(R))
    cols = list(range(C))

    # bfs
    queue.append(([], "", "", 0))
    if is_same([]):
        return 0
    while queue:
        changes, rs, cs, k = queue.popleft()

        # 행
        for r in rows:
            if str(r) not in list(rs):
                nchanges = changes[:]
                for c in cols:
                    if str(r) + str(c) not in changes: # 없었던 것은 추가
                        nchanges.append(str(r) + str(c))
                    else: # 있었던 것은 삭제
                        nchanges.remove(str(r) + str(c))
                if is_same(nchanges):
                    return k + 1
                queue.append((nchanges, rs + str(r), cs, k + 1))

        # 열
        for c in cols:
            if str(c) not in list(cs):
                nchanges = changes[:]
                for r in rows:
                    if str(r) + str(c) not in changes: # 없었던 것은 추가
                        nchanges.append(str(r) + str(c))
                    else: # 있었던 것은 삭제
                        nchanges.remove(str(r) + str(c))
                if is_same(nchanges):
                    return k + 1
                queue.append((nchanges, rs , cs + str(c), k + 1))
    return -1

print(solution( [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))