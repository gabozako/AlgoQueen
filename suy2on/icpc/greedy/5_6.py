## 회의실배치

import sys

input = sys.stdin.readline
N = int(input())
times = []
answer = 1

for _ in range(N):
    times.append(list(map(int, input().split())))

times = sorted(times, key=lambda x : (x[1],x[0])) # 끝나는시간, 시작하는 시간 순으로 정렬 : 시작하자마자 끝나는게 먼저 되버리면 안되기 때문에 시작시간도 고려해야함 

i = 1
bef = times[0]
while i < N:
    if bef[1] <= times[i][0]: # 다음 스케줄로 배치가능한면
        bef = times[i]
        answer += 1
    i += 1

print(answer)



