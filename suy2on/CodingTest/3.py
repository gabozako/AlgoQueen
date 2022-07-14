import collections


def solution(order):
    main = collections.deque()  # queue
    sub = []  # stack

    i = 0

    for j in range(1, len(order) + 1):
        main.append(j)

    while True:
        # 서브벨트부터
        while sub and sub[-1] == order[i]:
            sub.pop()
            i += 1

        # 메인벨트
        while main and order[i] != main[0]:
            sub.append(main.popleft())

        # 둘다 없는 경우
        if not main:
            return i

        # 메인에 순서 있는 경우
        else:
            main.popleft()
            i += 1

