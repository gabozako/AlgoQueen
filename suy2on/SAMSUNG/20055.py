## 컨베이어벨트
import sys
import collections

input = sys.stdin.readline

N, K = map(int, input().split())
A = collections.deque(map(int, input().split()))
robots = collections.deque([False] * (2*N))


t = 1
while True:
    ## 벨트회전
    A.rotate()
    robots.rotate()

    # TODO : 로봇 언제나 내리기
    # 내리기
    robots[N-1] = False

    ## 로봇이동
    for i in range(N-2, -1, -1):
        if robots[i]:
            if not robots[i + 1] and A[i + 1] >= 1:
                robots[i+1] = True
                robots[i] = False
                A[i + 1] -= 1
                # 내리기
                if i+1 == N-1:
                    robots[i+1] = False

    ## 로봇올리기
    if A[0] != 0:
        robots[0] = True
        A[0] -= 1



    cnt = 0
    ## 내구도 0인 칸 계산
    for i in range(2*N):
        if not A[i]:
            cnt += 1

    if cnt >= K:
        print(t)
        break

    t += 1





