## () 개수가 같으면 -> 균형잡힌 괄호 문자열
## () 짝도 맞다면 -> 올바른 괄호 문자열
def opposite(w):
    result = ""
    for c in w:
        if c == "(":
            result += ")"
        else:
            result += "("

    return result


def is_right(w):
    a, b = 0, 0
    for c in w:
        if c == "(":
            a += 1
        else:
            b += 1

        if a < b:
            return False

    return True


def solution(p):
    if not p:
        return p
    a, b = 0, 0
    i = 0
    while i < len(p):
        if p[i] == "(":
            a += 1
        else:
            b += 1

        i += 1
        if a == b:
            break

    u, v = p[0:i], p[i:]

    if is_right(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + opposite(u[1:-1])




