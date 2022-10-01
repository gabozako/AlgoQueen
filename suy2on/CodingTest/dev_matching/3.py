freqs = {
    2: 1,
    3: 1,
    4: 1,
    5: 3,
    6: 3,
    7: 1
}


def solution(k):
    result = []
    answer = 0

    dp = [-1] * (k + 1)
    for i in range(2, 8):
        if i < k + 1:
            dp[i] = freqs[i]

    def num_of_stick(numbers, num):
        global answer
        # 맞아 떨어지면
        if num == 0:
            result.append(numbers)
            return

            # 맞아 떨어지지 않으면
        if num < 0:
            return

        for n in freqs.keys():
            answer += dp[n] * num_of_stick(numbers + str(n), num - n)

    num_of_stick("", k)

    for arr in result:
        total = 1
        for i in range(1, len(arr)):
            total *= freqs[int(arr[i])]

        if arr[0] == "6" and len(arr) > 1:
            total *= 2
        else:
            total *= freqs[int(arr[0])]

        answer += total

    return answer