def time_to_second(time):
    hour, minute, second = map(int, time.split(":"))
    return hour * 3600 + minute * 60 + second


def second_to_time(time):
    hour, mod = divmod(time, 3600)
    minute, second = divmod(mod, 60)

    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = "0" + str(minute)
    else:
        minute = str(minute)

    if second < 10:
        second = "0" + str(second)
    else:
        second = str(second)

    return ":".join([hour, minute, second])


def solution(play_time, adv_time, logs):
    answer = 0
    finish = time_to_second(play_time)
    adv_time = time_to_second(adv_time)
    max_sum = 0

    totalSum = [0] * (finish + 1)

    # 광고누적합기록
    for log in logs:
        head, tail = log.split("-")
        head = time_to_second(head)
        tail = time_to_second(tail)

        totalSum[head] += 1
        totalSum[tail] -= 1

    # 누적합계산
    for i in range(1, finish):
        totalSum[i] += totalSum[i - 1]

    # 부분합기록
    subSum = []
    total = 0
    for i in range(finish):
        total += totalSum[i]
        subSum.append(total)

    # 구간중에 최대인것 구하기
    for i in range(finish - adv_time + 1):
        if i == 0:
            new_sum = subSum[i + adv_time - 1]
        else:
            new_sum = subSum[i + adv_time - 1] - subSum[i - 1]

        if max_sum < new_sum:
            max_sum = new_sum
            answer = i

    return second_to_time(answer)