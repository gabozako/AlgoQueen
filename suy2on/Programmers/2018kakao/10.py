# [3차] n진수 게임

change = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

# 숫자를 n진수로
def get_n_notation(num, n):
    if not num:
        return "0"
    result = ""
    while num:
        k, mod = divmod(num, n)
        if mod > 9:
            mod = change[mod]
        result = str(mod) + result
        num = k

    return result


def solution(n, t, m, p):
    answer = ''
    limit = m * (t - 1) + (p - 1) + 1
    nums = ""

    start = 0
    # 최대구해야하는 idx까지 계속해서 구하기
    while len(nums) < limit:
        nums += get_n_notation(start, n)
        start += 1

    # 출력할 인덱스만 따로 추출
    for i in range(t):
        answer += nums[m * i + (p - 1)]

    return answer