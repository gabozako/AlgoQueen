def solution(record):
    member = {}
    answer = []

    for r in record:
        req = r.split()
        if req[0] != "Leave":
            member[req[1]] = req[2]

    for r in record:
        req = r.split()
        if req[0] == "Enter":
            answer.append(member[req[1]] + "님이 " + "들어왔습니다.")
        elif req[0] == "Leave":
            answer.append(member[req[1]] + "님이 " + "나갔습니다.")

    return answer