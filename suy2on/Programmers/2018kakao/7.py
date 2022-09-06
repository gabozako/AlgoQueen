def solution(dartResult):
    idx = -1
    result = []
    pre = ""

    for char in dartResult:
        # 숫자면
        if char.isdigit():
            # 두자리수
            if pre.isdigit():
                score = 10
            else:
                idx += 1
                score = int(char)
        # 알파벳이면
        elif char.isalpha():
            if char == "S":
                result.append(score)
            elif char == "D":
                result.append(score ** 2)
            else:
                result.append(score ** 3)
        # 특수문자이면
        else:
            if char == "*":
                result[idx] *= 2
                if idx > 0:
                    result[idx - 1] *= 2
            else:
                result[idx] *= (-1)

        pre = char

    return sum(result)