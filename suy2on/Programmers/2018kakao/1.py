import collections


def start_ms(finish, T):
    hour, minute, second = finish.split(":")
    time = int(hour) * 3600000 + int(minute) * 60000 + float(second) * 1000
    time -= float(T[:-1]) * 1000

    return max(0, int(time + 1))


def time_to_ms(time):
    hour, minute, second = time.split(":")

    return int(int(hour) * 3600000 + int(minute) * 60000 + float(second) * 1000)


def solution(lines):
    answer = 1
    if len(lines) == 1:
        return answer

    records = []

    for line in lines:
        date, finish, T = line.split()

        start = start_ms(finish, T)
        finish = time_to_ms(finish)

        records.append([start, finish])

    for i, line in enumerate(lines):
        head = records[i][1]
        tail = head + 999
        cnt = 0
        for i in range(len(lines)):
            if records[i][0] > tail or records[i][1] < head:
                continue
            cnt += 1

        answer = max(cnt, answer)

    return answer