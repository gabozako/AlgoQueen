# 지면 2배, 이기면 다시 100원, 돈이 모자르면 전부
def solution(money, expected, actual):
    b_money = 0
    matching = True

    for exp, act in zip(expected, actual):
        # 배팅금액
        if matching:
            b_money = 100
        else:
            b_money *= 2

        # 배팅금액만큼 없을 때
        if money < b_money:
            b_money = money

        # 확인
        if exp == act:
            matching = True
            money += b_money
        else:
            matching = False
            money -= b_money

        # 돈 없으면 게임 끝
        if not money:
            break


    return money