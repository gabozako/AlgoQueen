## info = [10점개수, 9점개수 .., 0점개수]
import itertools
import collections
import math

def is_win(lion, info):
    li = 0
    ap = 0
    for i in range(11):
        if lion[i] == info[i] == 0:
            continue
        elif lion[i] > info[i]:
            li += i
        else:
            ap += i

    if li > ap:
        return li - ap
    else:
        return -1

def solution(n, info):
    info.reverse()
    max_diff = 0
    answer = []


    for lion in itertools.combinations_with_replacement(range(11),n):
        lion = collections.Counter(lion)

        win = is_win(lion, info)
        if win != -1: # 이겼다면
            if max_diff < win:
                max_diff = win
                answer = lion

    if max_diff:
        result = [0] * 11
        for key in answer.keys():
            result[key] = answer[key]
        return list(reversed(result))
    else:
        return [-1]


print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))



math.ceil()