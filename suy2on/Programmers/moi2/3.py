import itertools


def solution(word):
    answer = 0

    words = []
    for i in range(1, 6):
        for permu in itertools.product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append("".join(permu))

    words.sort()

    return words.index(word) + 1