import collections
import math


def time_to_minute(time):
    t, m = time.split(":")
    return int(t) * 60 + int(m)


def solution(fees, records):
    answer = []
    parkingTimes = collections.defaultdict(list)

    for record in records:
        time, number, action = record.split()
        parkingTimes[number].append(time_to_minute(time))

    for car in sorted(parkingTimes.keys()):
        total = 0
        if len(parkingTimes[car]) % 2 == 1:  ## 마지막 출차기록 없으면 23:59
            parkingTimes[car].append(23 * 60 + 59)
        for i in range(0, len(parkingTimes[car]), 2):
            total += parkingTimes[car][i + 1] - parkingTimes[car][i]

        if total <= fees[0]:  # 기본요금
            answer.append(fees[1])

        else:
            answer.append(fees[1] + math.ceil((total - fees[0]) / fees[2]) * fees[3])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))