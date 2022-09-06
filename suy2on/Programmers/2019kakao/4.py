# 정확성통과
def solution(food_times, k):
    # 예외처리
    if sum(food_times) <= k:
        return -1


    linkedList = [[i - 1, i + 1] for i in range(len(food_times))]
    linkedList[-1][1] = 0
    linkedList[0][0] = len(food_times) - 1

    p = 0
    for i in range(k):
        food_times[p] -= 1
        if not food_times[p]:
            linkedList[linkedList[p][0]][1] = linkedList[p][1]
            linkedList[linkedList[p][1]][0] = linkedList[p][0]
        p = linkedList[p][1]

    return p + 1

# 효율성

def solution(food_times, k):
    # 예외처리
    if sum(food_times) <= k:
        return -1

    food_pairs = []
    for i in range(len(food_times)):
        food_pairs.append([food_times[i], i])

    food_pairs.sort()

    pre = 0
    for i in range(len(food_pairs)):
        total = (food_pairs[i][0] - pre) * (len(food_pairs) - i)
        if k <= total:
            idx = k % (len(food_pairs) - i)
            food_pairs2 = sorted(food_pairs[i:], key=lambda x: x[1])
            return food_pairs2[idx][1] + 1
        else:
            k -= total
            pre = food_pairs[i][0]



def solution(food_times, k):
    # 예외처리
    if sum(food_times) <= k:
        return -1

    food_pairs = []
    for i in range(len(food_times)):
        food_pairs.append([food_times[i], i])

    food_pairs.sort()

    first = food_pairs[0][0] * len(food_pairs)
    p = 0
    if k >= first:
        k -= first
        p = 1
        while p < len(food_pairs):
            total = (food_pairs[p][0] - food_pairs[p - 1][0]) * (len(food_pairs) - p)
            if k < total:
                break
            k -= total
            p += 1
    idx = k % (len(food_pairs) - p)
    food_pairs2 = sorted(food_pairs[p:], key=lambda x: x[1])

    return food_pairs2[idx][1] + 1





