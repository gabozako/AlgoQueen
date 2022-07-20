def solution(s):
    stack = []
    # 순서대로 제거
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 다 제거 됐으면 문자열길이로 성공여부결정

    return int(len(stack) == 0)