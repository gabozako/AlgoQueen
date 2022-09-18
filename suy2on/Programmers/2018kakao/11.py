## [3차] 파일명 정렬


def solution(files):
    answer = []
    fs = []

    for file in files:
        head = ""
        number = ""

        i = 0
        # HEAD
        while i < len(file):
            if file[i].isdigit():
                break
            head += file[i]
            i += 1

        # NUMBER
        while i < len(file):
            if not file[i].isdigit():
                break
            number += file[i]
            i += 1

        fs.append([head.lower(), int(number), file])

    return [i[2] for i in sorted(fs, key=lambda x: (x[0], x[1]))]