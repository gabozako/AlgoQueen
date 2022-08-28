def solution(N, stages):
    answer = []
    freqs = [0] * (N + 1)

    for stage in stages:
        freqs[stage - 1] += 1

    for i in range(N):
        approach = sum(freqs[i:])
        if approach:
            answer.append([freqs[i] / approach, i + 1])
        else:
            answer.append([0, i + 1])

    return [a[1] for a in sorted(answer, key=lambda x: (-x[0], x[1]))]