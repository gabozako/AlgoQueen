def solution(bricks):
    answer = []

    for i in range(len(bricks)):
        w = sum(bricks[:i + 1])
        total = w
        h = 0
        clear = True
        # 위층 쌓기
        for j in range(i + 1, len(bricks)):
            if total == w:
                total = 0
                h += 1
            elif total > w:
                clear = False
                break
            total += bricks[j]
        # 마지막검사
        if total == w and clear:
            answer.append(h + 1)

    return sorted(answer)