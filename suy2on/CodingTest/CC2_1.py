import collections
import itertools

def solution(number):
    answer = 0
    for students in itertools.combinations(number,3):
        if not sum(students):
            answer += 1

    return answer