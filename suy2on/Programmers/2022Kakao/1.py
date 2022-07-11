import collections


def solution(id_list, report, k):
    send = collections.defaultdict(set)
    receive = collections.defaultdict(set)
    over = []
    answer = []

    for r in report:
        user1, user2 = r.split()
        send[user1].add(user2)
        receive[user2].add(user1)

    for name in id_list:
        if len(receive[name]) >= k:
            over.append(name)

    ## 받게 될 메일 수
    for name in id_list:
        cnt = 0
        for n in send[name]:
            if n in over:
                cnt += 1
        answer.append(cnt)

    return answer