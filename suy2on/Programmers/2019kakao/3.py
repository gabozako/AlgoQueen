import collections
import itertools


def solution(relation):
    N = len(relation[0])
    K = len(relation)
    cks = collections.defaultdict(list)
    nums = range(N)

    # 희소
    for i in range(1, N+1):
        for combi in itertools.combinations(nums, i):
            freqs = collections.defaultdict(int)
            for r in relation:
                string = ""
                for c in combi:
                    string += r[c]
                freqs[string] += 1
            if len(freqs) == K: # 희소성
                cks[i].append(combi)


    # 최소
    for i in range(1,N):
        for ck1 in cks[i]:
            for j in range(i+1,N+1):
                tmp = []
                for ck2 in cks[j]:
                    isMin = False
                    for c in ck1:
                        if c not in ck2:
                            isMin = True
                    if isMin:
                        tmp.append(ck2)
                cks[j] = tmp

    answer = 0
    for i in range(1,N+1):
        answer += len(cks[i])

    return answer