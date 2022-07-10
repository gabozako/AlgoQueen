import itertools
import collections


def solution(orders, course):import itertools
import collections


def solution(orders, course):
    answer = []
    menus = collections.defaultdict(list)

    for order in orders:
        for num in course:
            if len(order) < num:
                break
            for foodSet in itertools.combinations(order, num):
                menus[num].append("".join(foodSet))

    for num in course:
        freqs = collections.Counter(menus[num]).most_common(len(menus[num]))
        for freq in freqs:
            if freq[1] == freqs[0][1]:
                answer.append(freq[0])

    return sorted(answer)

    answer = []
    menus = collections.defaultdict(list)

    for order in orders:
        for num in course:
            if len(order) < num:
                break
            for foodSet in itertools.combinations(order, num):
                menus[num].append("".join(foodSet))

    for num in course:
        freqs = collections.Counter(menus[num]).most_common(len(menus[num]))
        for freq in freqs:
            if freq[1] == freqs[0][1]:
                answer.append(freq[0])

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
