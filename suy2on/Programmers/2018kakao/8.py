def to_playtime(start, end):
    hour, minute = start.split(":")
    start = int(hour) * 60 + int(minute)

    hour, minute = end.split(":")
    end = int(hour) * 60 + int(minute)

    return end - start


def change_code(string):
    return string.replace("A#", "H").replace("C#", "I").replace("D#", "J").replace("F#", "K").replace("G#", "L")


def solution(m, musicinfos):
    answer = []

    for music in musicinfos:
        start, end, title, sheet = music.split(",")
        playtime = to_playtime(start, end)

        # 재생음악출력
        sheet = change_code(sheet)
        cnt, mod = divmod(playtime, len(sheet))
        song = sheet * cnt + "".join(sheet[:mod])

        # 찾기
        if change_code(m) in song:
            answer.append([playtime, title])

    if answer:
        return sorted(answer, key=lambda x: -x[0])[0][1]

    else:
        return "(None)"