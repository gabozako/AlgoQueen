def solution(money, minratio, maxratio, ranksize, threshold, months):

    for _ in range(months):
        # 소유 가정금액
        extra = money % 100
        s_money = money - extra


        # 소유 가정금액이 threshold미만이면 걷지 않음
        if s_money >= threshold:
            # 세금징수 : ranksize 단위만큼 상승할 때 마다 1퍼씩 추가
            extra = s_money - threshold
            add_percent = extra // ranksize
            # 상한 적용
            percent = min(maxratio, minratio + add_percent)
            money -= (s_money * percent) / 100



    return money