import collections

# 비교
def is_subString(dic1, dic2):
    if sorted(dic1.keys()) != sorted(dic2.keys()):
        return False
    for key in dic1.keys():
        if dic1[key] != dic2[key]:
            return False
    return True

def solution(S, pattern):
    answer = 0
    pattern_freq = dict(collections.Counter(pattern))
    N = len(pattern)

    # N길이 만큼 슬라이싱 윈도우
    for i in range(len(S)-N+1):
        if is_subString(dict(collections.Counter(S[i:i+N])), pattern_freq):
            answer += 1


    return answer