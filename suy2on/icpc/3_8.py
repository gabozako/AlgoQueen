## 공유기 설치
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input()))

# 집 정렬
houses.sort()
distances = []

left = 1
right = houses[-1] - houses[0]

# 최대거리를 이분탐색으로 찾기
while left <= right:
    mid = (left + right) // 2
    cnt = 1 # 첫번째는 무조건 포함 M개 넘어도 되니까
    i = 0
    j = 1
    while j < N:
        if houses[j] - houses[i] >= mid:
            cnt += 1
            i = j

        j += 1

    # 공유기가 제한 이상이면
    if cnt >= M:
        left = mid + 1 # 간격 늘려보기
    else:
        right = mid - 1 # 간격 줄여보기

print(right) # 제한이랑 같아도 오른쪽으로 넘겼기 때문에 결국에는 right가 가는쪽으로 가는게 맞다
