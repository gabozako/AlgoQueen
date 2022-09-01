import itertools


def solution(numbers):
    answer = set()
    for combi in itertools.combinations(numbers, 2):
        answer.add(sum(combi))

    return sorted(answer)