import itertools

def solution(receive, sell):
    answer = []
    max_cnt = -1
    n = len(sell)

    for visit in itertools.product(range(n), repeat=5):
        cnt = 0
        stocks = [0] * len(sell)
        for i in range(5):
            # 각 shop 일반판매
            for j in range(len(sell)):
                stocks[j] = max(0, stocks[j] + receive[j][i] - sell[j][i])

            # 방문 shop에서 옷 다사기
            cnt += stocks[visit[i]]
            stocks[visit[i]] = 0

        if max_cnt < cnt:
            max_cnt = cnt
            answer = visit


    return answer