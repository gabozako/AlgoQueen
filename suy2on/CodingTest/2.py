# 원하는 물품을 원하는 수량으로 10일간 연속으로 구매가능한 날짜 세기
# 없으면 0
import collections


def solution(want, number, discount):
    answer = 0
    wantDict = collections.defaultdict(int)
    discountDict = collections.defaultdict(int)

    # 구매가능여부확인
    def is_ok(a, b):
        for key in a.keys():
            if a[key] != b[key]:
                return False

        return True

    # 원하는물품 수량기록
    for i in range(len(want)):
        wantDict[want[i]] = number[i]

    # 세일물품 수량기록
    for i in range(10):
        discountDict[discount[i]] += 1

    if is_ok(wantDict, discountDict):
        answer += 1

    head, tail = 0, 10

    # 슬라이딩 윈도우
    while tail < len(discount):
        discountDict[discount[head]] -= 1
        head += 1
        discountDict[discount[tail]] += 1
        tail += 1

        if is_ok(wantDict, discountDict):
            answer += 1

    return answer