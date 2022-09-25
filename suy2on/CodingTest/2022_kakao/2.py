import heapq

def solution(cap, n, deliveries, pickups):
    pq_d = []
    pq_p = []
    answer = 0

    for i, delivery in enumerate(deliveries):
        if delivery:
            heapq.heappush(pq_d, [-i,delivery])

    for i, pickup in enumerate(pickups):
        if pickup:
            heapq.heappush(pq_p, [-i,pickup])



    while pq_d or pq_p:
        print(pq_d)
        print(pq_p)
        d_cnt = 0
        d_dis = 0

        p_cnt = 0
        p_dis = 0
        while pq_d and d_cnt + pq_d[0][1] < cap:
            dis, product = heapq.heappop(pq_d)
            d_cnt += product
            d_dis = max(d_dis, -1 * dis)

        if d_cnt < cap and pq_d:
            dis, product = heapq.heappop(pq_d)
            heapq.heappush(pq_d, [dis, product - (cap - d_cnt)])
            d_cnt = cap

        while pq_p and p_cnt + pq_p[0][1] < cap:
            dis, product = heapq.heappop(pq_p)
            p_cnt += product
            p_dis = max(p_dis, -1 * dis)

        if p_cnt < cap and pq_p:
            dis, product = heapq.heappop(pq_p)
            heapq.heappush(pq_p, [dis, product - (cap - p_cnt)])
            p_cnt = cap

        answer += max(p_dis+1, d_dis+1) * 2




    return answer


print(solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0]))