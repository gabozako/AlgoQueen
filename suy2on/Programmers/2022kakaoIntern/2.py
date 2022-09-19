import collections


def solution(queue1, queue2):
    answer = 0

    q1 = collections.deque(queue1)
    q2 = collections.deque(queue2)

    sq1 = sum(q1)
    sq2 = sum(q2)

    # 둘로 나눠지지 않으면
    if (sq1 + sq2) % 2:
        return -1

    while sq1 != sq2:
        if sq1 > sq2:
            move = q1.popleft()
            q2.append(move)
            sq1 -= move
            sq2 += move

        elif sq2 > sq1:
            move = q2.popleft()
            q1.append(move)
            sq1 += move
            sq2 -= move

        answer += 1

        # 하나라도 비면
        if not sq1 or not sq2:
            return -1

        # 계속 찾아도 안됐을 때
        if answer > (len(q1) + len(q2)) * 2:
            return -1

    return answer