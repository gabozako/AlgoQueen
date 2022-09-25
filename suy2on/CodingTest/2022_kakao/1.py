def date_to_day(date):
    year, month, day = map(int, date.split("."))

    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    today = date_to_day(today)
    expiration = {}

    for term in terms:
        name, period = term.split()

        expiration[name] = int(period) * 28

    for i, privacy in enumerate(privacies):
        start, ty = privacy.split()
        start = date_to_day(start)
        if start + expiration[ty] >= today:
            answer.append(i)


    return answer