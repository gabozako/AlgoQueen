import bisect
import collections


def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    initial_players.sort()
    ranking = collections.deque()
    for player in initial_players[-rank:]:
        ranking.append(player)

    answer = ranking[0]

    for new_player in new_players:
        idx = bisect.bisect_left(ranking, new_player)
        if idx:
            ranking.insert(idx, new_player)
            ranking.popleft()

        answer += ranking[0]

    return answer