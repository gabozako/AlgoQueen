class Node:
    def __init__(self, num, pre = None, nxt = None):
        self.num = num
        self.pre = pre
        self.nxt = nxt


def solution(n, k, cmd):
    trashcan = []
    cur = None

    # 링크드리스트 초기화
    p = root = Node(0)
    for i in range(1,n):
        p.nxt = Node(i,p)
        p = p.nxt
        # 초기위치기억
        if i == k:
            cur = p

    # 명령어 시작
    for c in cmd:
        sc = c.split()

        if sc[0] == "U":
            for _ in range(int(sc[1])):
                cur = cur.pre
        elif sc[0] == "D":
            for _ in range(int(sc[1])):
                cur = cur.nxt
        elif sc[0] == "C":
            trashcan.append(cur)
            cur.nxt.pre = cur.pre
            cur.pre.nxt = cur.nxt
            if cur.nxt:
                cur = cur.nxt
            else:
                cur = cur.pre
        else:
            save = trashcan.pop()
            save.pre.nxt = save
            save.nxt.pre = save


    answer = ["O"] * n
    while trashcan:
        answer[trashcan.pop().num] = "X"


    return "".join(answer)