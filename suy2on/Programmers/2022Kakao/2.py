import itertools


def solution(n, info):
    answer = []

    # 어피치 뒤집기 -> 0부터 10점까지
    info.reverse()

    # 중복조합으로 던질 수 있는 모든 경우를 계산
    for combi in itertools.combinations_with_replacement(range(11), n):
        info_R = [0] * 11
        for c in combi:
            info_R[c] += 1

        # 점수계산시작
        score_A = 0
        score_R = 0
        for score in range(1, 11):
            if info[score] == info_R[score] == 0:
                continue
            if info[score] >= info_R[score]:
                score_A += score
            else:
                score_R += score

        # 라이언이 이겼다면
        if score_R > score_A:
            answer.append([score_R - score_A, info_R])

    # 라이언이 이길 수 없다면
    if not len(answer):
        return [-1]

    return sorted(answer, key=lambda x: (x[0], x[1]), reverse=True)[0][1][::-1]