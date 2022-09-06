def solution(n):
    # 3진법으로 바꾸기
    three = ""
    while n > 2:
        n, mod = divmod(n, 3)
        three = str(mod) + three

    three = str(n) + three

    # 반전 10진법으로 바꾸기
    answer = 0
    for i in range(len(three)):
        answer += int(three[i]) * 3 ** i

    return answer