## 소트
N = int(input())
numbers = list(map(int, input().split()))
S = int(input())

start = 0
# 교환횟수가 남거나 인덱스 범위 안인 경우
while start < N and S:
    # S안에서 최대치 찾기
    maxVal = max(numbers[start:start + S+1])
    maxPos = numbers.index(maxVal)

    # 최대 범위 맨앞으로 보내기
    p = maxPos
    for _ in range(maxPos-start):
        numbers[p], numbers[p-1] = numbers[p-1], numbers[p]
        p -= 1
        S -= 1

    # 스타트 하나 옮기기
    start = p + 1

print(*numbers)



