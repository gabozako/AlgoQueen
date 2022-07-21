## 이진탐색
N = int(input())
have = list(map(int, input().split()))
M = int(input())
numbers = map(int, input().split())
answer = []
have.sort()

def bisect(target, left, right):
    if left > right:
        answer.append(0)
        return

    mid = left + (right - left) // 2
    if have[mid] == target:
        answer.append(1)
        return

    elif have[mid] < target:
        bisect(target, mid+1, right)

    else:
        bisect(target, left, mid-1)

for number in numbers:
    bisect(number, 0, N-1)

print(*answer)
