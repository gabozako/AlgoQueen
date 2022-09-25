# 동의 비동의
import collections


def solution(survey, choices):
    answer = ''
    index = collections.defaultdict(int)

    for s, c in zip(survey, choices):
        k, mod = divmod(c, 4)
        if mod:
            index[s[abs(k - 1)]] += mod

    if index[R] > index[T]:
        answer += "R"
    else:
        answer += "T"
    if index[C] > index[F]:
        answer += "C"
    else:
        answer += "F"
    if index[J] > index[M]:
        answer += "J"
    else:
        answer += "M"
    if index[A] > index[N]:
        answer += "A"
    else:
        answer += "N"

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))