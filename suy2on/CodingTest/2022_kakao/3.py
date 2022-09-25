import itertools


def solution(users, emoticons):
    answer = [0,0]
    discount_rate = [10,20,30,40]

    for discount in itertools.product(discount_rate, repeat=len(emoticons)):
        discount_emoticons = []
        plus = 0
        total_cost = 0
        for emoticon, dis in zip(emoticons,discount):
            discount_emoticons.append(emoticon * (100 - dis) * 0.01)

        for user in users:
            cost = 0
            for dis, dis_emoticon in zip(discount, discount_emoticons):
                if dis >= user[0]:
                    cost += dis_emoticon

            if cost >= user[1]:
                plus += 1
            else:
                total_cost += cost

        answer = max(answer, [plus, total_cost])


    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))