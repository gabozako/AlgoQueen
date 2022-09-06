def solution(cacheSize, cities):
    answer = 0
    if not cacheSize:
        return len(cities) * 5
    queue = []
    for city in cities:
        city = city.lower()
        try: # hit
            idx = queue.index(city)
            queue.append(queue.pop(idx))
            answer += 1
        except: # miss
            answer += 5
            if len(queue) >= cacheSize:
                queue.pop(0)
            queue.append(city)
    return answer