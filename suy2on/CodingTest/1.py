# 존재하지 않은 경우 -> -1
# 모두 0인 경우 -> 0
# 이외 -> 가장 큰수 : 매번 가장 큰 수를 앞에다가 더하면 큰수가된다.
import collections
import heapq


def solution(X, Y):
    answer = ''
    freqs1 = dict(collections.Counter(X))
    freqs2 = dict(collections.Counter(Y))

    X = list(X)
    Y = list(Y)

    both = []
    for char in set(X + Y):
        if char in freqs1 and char in freqs2:  # 둘다 있는 것이면
            for _ in range(min(freqs1[char], freqs2[char])):
                heapq.heappush(both, int(char))

    if not both:  # 겹치는 것이 없는 경우
        return "-1"

    elif not sum(both):  # 모두 0인경우
        return "0"

    else:  # 그외
        while both:
            answer = answer + str(heapq.heappop(both))

        return answer[::-1]

