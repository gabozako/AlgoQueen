import collections
import bisect

def solution(info, query):
    combis = collections.defaultdict(list)
    answer = []

    # 가능한 모든 조합에 점수 더해주기
    for i in info:
        lang, pos, career, food, score = i.split()
        for l in [lang, "-"]:
            for p in [pos, "-"]:
                for c in [career, "-"]:
                    for f in [food, "-"]:
                        combis[l+p+c+f].append(int(score))

    # 정렬
    for combi in combis.keys():
        combis[combi].sort()

    # 쿼리검색
    for q in query:
        q = q.replace("and", "")
        q = q.split()
        s = q[-1]
        combi = "".join(q[:-1])

        scores = combis[combi]
        head = bisect.bisect_left(scores,int(s),0)
        answer.append(len(scores) - head)

    return answer

