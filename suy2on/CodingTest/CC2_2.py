import collections


def solution(topping):
    answer = 0
    part1 = collections.defaultdict(int)
    part2 = collections.defaultdict(int)
    for t in topping:
        part2[t] += 1

    type1 = set()
    type2 = set(part2.keys())

    for t in topping:
        if part1[t] == 0:
            type1.add(t)
        part1[t] += 1

        part2[t] -= 1
        if part2[t] == 0:
            type2.remove(t)

        if len(type2) == len(type1):
            answer += 1

    return answer