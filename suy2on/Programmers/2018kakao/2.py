def time_to_minute(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def minute_to_time(minute):
    hour, minute = divmod(minute, 60)

    hour = str(hour)
    minute = str(minute)

    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute

    return hour + ":" + minute


def solution(n, t, m, timetable):
    timetable.sort()
    arrive_time = time_to_minute("09:00")

    for _ in range(n - 1):
        cnt = 0
        while timetable and cnt < m and time_to_minute(timetable[0]) <= arrive_time:
            timetable.pop(0)
            cnt += 1

        arrive_time += t

    # 마지막버스
    people = []
    while timetable and len(people) < m and time_to_minute(timetable[0]) <= arrive_time:
        people.append(timetable.pop(0))

    if len(people) == m:
        return minute_to_time(time_to_minute(people.pop()) - 1)

    else:
        return minute_to_time(arrive_time)

