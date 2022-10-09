import collections


def solution(logs, events):
    user_log = collections.defaultdict(list)

    for log in logs:
        time, name, action = log.split()
        user_log[name].append(action)



    answer = []
    for user in user_log.keys():
        check = [False] * len(events)

        for action in user_log[user]:
            # 중복
            if check[events.index(action)]:
                answer.append(user)
                break

            # 순서대로
            if events.index(action) != 0 and not check[events.index(action)-1]:
                answer.append(user)
                break

            check[events.index(action)] = True


    return sorted(answer) if answer else ["-1"]