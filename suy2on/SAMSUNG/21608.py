import sys
import collections

input = sys.stdin.readline

N = int(input())
students = []
favorites = {}
seats = [[0] * N for _ in range(N)]
drc = [[1,0],[-1,0],[0,1],[0,-1]]

for _ in range(N ** 2):
    info = list(map(int, input().split()))
    students.append(info[0])
    favorites[info[0]] = info[1:]



def is_valid(i, j):
    if 0 <= i <= N - 1 and 0 <= j <= N - 1:
        return True
    return False


def where_to_sit(number):
    result = collections.defaultdict(list)

    for i in range(N):
        for j in range(N):
            if not seats[i][j]:
                cnt = 0
                blank = 0
                # 인접자리 검사
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni,nj):
                        # 빈자리
                        if not seats[ni][nj]:
                            blank += 1
                        # 좋으하는 사람
                        elif seats[ni][nj] in favorites[number]:
                            cnt += 1

                result[cnt].append([blank,i,j])

    # 좋아하는 사람 많은 빈칸으로
    max_cnt = max(result.keys())

    return sorted(result[max_cnt], key=lambda x : (-x[0], x[1], x[2]))[0]


for s in students:
    here = where_to_sit(s)
    seats[here[1]][here[2]] = s

# 만족도 조사
answer = 0
for i in range(N):
    for j in range(N):
        num = seats[i][j]
        cnt = 0
        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]
            if is_valid(ni, nj):
                if seats[ni][nj] in favorites[num]:
                    cnt += 1
        if cnt:
            answer += 10**(cnt-1)

print(answer)

















