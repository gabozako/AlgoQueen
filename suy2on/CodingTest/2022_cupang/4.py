# 가로 세로 제외 말이 움직일 수 있는 곳
def can_move(r,c):
    move = set()
    move.add((r+2,c+1))
    move.add((r+2,c-1))
    move.add((r-2,c+1))
    move.add((r-2,c-1))

    move.add((r+1,c+2))
    move.add((r+1,c-2))
    move.add((r-1,c+2))
    move.add((r-1,c-2))

    return move


answer = 0

def solution(n, blocks):
    rook_knights = []
    status = [[True] * n for _ in range(n)]

    # 못가는 곳
    for br,bc in blocks:
        status[br-1][bc-1] = False

    def locate(r):
        global answer

        if r == n:
            answer += 1
            return

        for c in range(n):
            if status[r][c]:
                condition = True
                # 배치가능한지 보기 : 세로, 나머지 체크
                for i,j in rook_knights:
                    if c == j or (r,c) in can_move(i,j):
                        condition = False
                        break

                # 가능하면 넣기
                if condition:
                    rook_knights.append([r,c])
                    locate(r+1)
                    # 백트래킹
                    rook_knights.remove([r,c])


    locate(0)
    return answer