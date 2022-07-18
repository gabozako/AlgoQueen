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

    def is_same(rs, cs):
        changes = []
        rs = list(rs)
        cs = list(cs)
        for r in rs:
            for c in range(C):
                if str(c) not in cs:
                    changes.append(r + str(c))

        for c in cs:
            for r in range(R):
                if str(r) not in rs:
                    changes.append(str(r) + c)

        changes.sort()
        if len(changes) == len(haveToChange):
            print(changes)
            print(haveToChange)
            for i in range(len(changes)):
                if changes[i] != haveToChange[i]:
                    return False
            return True

        return False

    rows = list(range(R))
    cols = list(range(C))

    queue.append(("", "", 0))
    while queue:
        rs, cs, k = queue.popleft()
        if is_same(rs, cs):
            return k

        print("---")
        for r in rows:
            if str(r) not in list(rs):
                queue.append((rs + str(r), cs, k + 1))
                print(r)
        for c in cols:
            if str(c) not in list(cs):
                queue.append((rs, cs + str(c), k + 1))
                print(c)
    return -1


print(solution( [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))