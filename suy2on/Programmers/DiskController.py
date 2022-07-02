# 처음에 들어온 작업부터 시작
# 작업 끝날 때까지 들어온 작업들 길이순으로 저장 -> PQ
import heapq


def solution(jobs):
    answer = 0

    N = len(jobs)
    jobs = sorted(jobs, reverse=True)
    print(jobs)
    waiting = []
    job = jobs.pop()
    heapq.heappush(waiting, (job[1], job[0]))
    time, totalTime = 0, 0
    while waiting:
        during, start = heapq.heappop(waiting)
        time = max(time + during, start + during)
        totalTime += time - start

        ## 큐에넣기
        while jobs and time >= jobs[-1][0]:
            job = jobs.pop()
            heapq.heappush(waiting, (job[1], job[0]))

        if jobs and not waiting:
            job = jobs.pop()
            heapq.heappush(waiting, (job[1], job[0]))

    return totalTime // N