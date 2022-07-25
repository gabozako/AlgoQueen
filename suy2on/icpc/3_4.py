# 숫자카드 2
import bisect

N = int(input())
have = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
answer = []

have.sort()

def bisect_left(left, right, target):
    mid = (left + right) // 2
    if left < right:
        if have[mid] >= target:
            return bisect_left(left, mid, target)
        else:
            return bisect_left(mid+1, right, target)
    else:
        if have[mid] == target:
            return mid
        else:
            return -1


def bisect_right(left, right, target):
    mid = (left + right + 1) // 2
    if left < right:
        if have[mid] > target:
            return bisect_right(left,mid-1, target)
        else:
            return bisect_right(mid, right, target)
    else:
        if have[mid] == target:
            return mid
        else:
            return -1



# for number in numbers:
#     left = bisect_left(0, N-1, number)
#     if left == -1:
#         answer.append(0)
#         continue
#     right = bisect_right(0, N-1, number)
#     answer.append(right-left+1)

for number in numbers:
    left = bisect.bisect_left(have,number)
    right = bisect.bisect_right(have, number)
    answer.append(right-left)


print(*answer)

