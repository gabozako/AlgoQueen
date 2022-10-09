import collections

def solution(cards, shuffles):
    answer = 0
    visited = [False] * (len(cards)+1)


    for i in range(len(cards)):
        # cycle찾기
        if not visited[i+1]:
            cycle = [cards[i]]
            visited[i+1] = True
            j = shuffles[i]

            while not visited[j]:
                cycle.append(cards[j-1])
                visited[j] = True
                j = shuffles[j-1]

            # cycle 숫자 빈도 체크
            freqs = collections.Counter(cycle).most_common()
            if len(freqs) == 1:
                continue

            # 빈도 가장 많은 것으로 모두 바꾸기
            for freq in freqs[1:]:
                answer += freq[1]



    return answer
