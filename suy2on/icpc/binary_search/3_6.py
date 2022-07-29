# 나무자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))
left = 0
right = max(trees)

def is_ok(h):
    total = 0
    for tree in trees:
        total += max(tree - h, 0)

    return total >= M


while left <= right:
    mid = (left + right) // 2
    if is_ok(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)





# import bisect
#
# N, M = map(int, input().split())
# trees = list(map(int, input().split()))
# trees.sort()
# H = trees[-1]
# get = 0
#
# while H > 0:
#     H -= 1
#     get += (N - bisect.bisect_right(trees, H))
#     if get >= M:
#         break
#
# print(H)
