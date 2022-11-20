import collections


def solution(jobs):
    answer = []
    jobs = collections.deque(jobs)

    cur = 0
    wq = {}
    # 지금 일하고 있는 작업번호
    work_num = 0
    while True:
        # 새로운 일 추가
        extra = 0
        while jobs and cur >= jobs[0][0]:
            req, time, num, imp = jobs.popleft()
            if num in wq:
                wq[num][0] += imp
                wq[num][2] += time
            else:
                # 같은부류일
                if work_num == num:
                    extra += time
                    continue
                wq[num] = [imp, num, time]


        # 연장근무 없으면 새로운 일 찾기
        if not extra:
            if not wq:
                # 다음에 할일 없으면 시간흐르기
                if jobs:
                    cur += 1
                    work_num = 0
                # 일이 모두 끝남
                else:
                    break
            else:
                # 중요도와 분류번호 순으로 정렬
                next_job = sorted(list(wq.values()), key=lambda x: (-x[0], x[1]))[0]
                del wq[next_job[1]]
                cur += next_job[2]
                work_num = next_job[1]
                if answer and answer[-1] == next_job[1]:
                    continue
                answer.append(next_job[1])

        # 연장근무
        else:
            cur += extra

    return answer


print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))