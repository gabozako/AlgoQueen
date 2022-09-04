
# 정확성 통과
def solution(n, k, cmd):
    li = [True] * n
    trashcan = []

    for c in cmd:
        c = c.split()

        if c[0] == "D":
            cnt = 0
            while cnt < int(c[1]):
                k += 1
                if li[k]:
                    cnt += 1

        elif c[0] == "U":
            cnt = 0
            while cnt < int(c[1]):
                k -= 1
                if li[k]:
                    cnt += 1

        elif c[0] == "C":
            li[k] = False
            trashcan.append(k)
            # 아래로 찾기
            p = k + 1
            while p < n and not li[p]:
                p += 1

            # 끝에 도달 했으면
            if p >= n:
                # 위로 찾기
                p = k - 1
                while p > -1 and not li[p]:
                    p -= 1

            k = p

        else:
            li[trashcan.pop()] = True

    answer = ""
    for i in li:
        if i:
            answer += "O"
        else:
            answer += "X"

    return answer

# 효율성 통과

def solution(n, k, cmd):
    li = [[True, i - 1, i + 1] for i in range(n)]
    trashcan = []

    def is_valid(num):
        if 0 <= num <= n - 1:
            return True
        return False

    for c in cmd:
        c = c.split()

        if c[0] == "D":
            for i in range(int(c[1])):
                k = li[k][2]

        elif c[0] == "U":
            for i in range(int(c[1])):
                k = li[k][1]

        elif c[0] == "C":
            li[k][0] = False
            trashcan.append(k)

            # 이어주기
            if is_valid(li[k][1]):
                li[li[k][1]][2] = li[k][2]
            if is_valid(li[k][2]):
                li[li[k][2]][1] = li[k][1]

            if is_valid(li[k][2]):
                k = li[k][2]
            else:
                k = li[k][1]

        else:
            rc = trashcan.pop()
            li[rc][0] = True
            # 다시이어주기
            if is_valid(li[rc][1]):
                li[li[rc][1]][2] = rc
            if is_valid(li[rc][2]):
                li[li[rc][2]][1] = rc

    answer = ""
    for i in li:
        if i[0]:
            answer += "O"
        else:
            answer += "X"

    return answer