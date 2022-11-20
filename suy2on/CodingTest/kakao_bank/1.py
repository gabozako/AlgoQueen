def solution(logs):
    answer = [0] * 24
    # 구분
    logs = logs.split("\n")

    for log in logs:
        date, time = log.split()
        hour, minute, second = map(int, time.split(":"))

        # 시간보정
        hour = (hour + 9) % 24
        answer[hour] += 1


    return answer