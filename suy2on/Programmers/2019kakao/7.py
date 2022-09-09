import collections

def solution(board):
    answer = 0
    N = len(board)

    for i in range(N):
        print(board[i])

    blocks = collections.defaultdict(list)
    types = [
        # 첫번째
        [[0, 1], [0, 2], [1, 2]],
        [[0, 1], [1, 0], [2, 0]],
        [[1, 0], [1, 1], [1, 2]],
        [[1, 0], [2, -1], [2, 0]],
        # 두번째
        [[0, 1], [0, 2], [1, 0]],
        [[1, 0], [2, 0], [2, 1]],
        [[1, -2], [1, -1], [1, 0]],
        [[0, 1], [1, 1], [2, 1]],
        ## 세번째
        [[1, -1], [1, 0], [1, 1]],
        [[1, 0], [1, 1], [2, 0]],
        [[0, 1], [0, 2], [1, 1]],
        [[1, -1], [1, 0], [2, 0]]
    ]

    remove_by_type = {
        2: [[0, 1], [0, 2]],
        3: [[1, -1]],
        5: [[1, 1]],
        6: [[0, -2], [0, -1]],
        8: [[0, -1], [0, 1]]
    }

    # 블럭위치파악
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                blocks[board[i][j]].append([i, j])

    # 블럭타입파악
    block_by_type = {}
    for block in blocks.values():
        print(block)
        block.sort()
        # 기준블록으로부터 변화량으로 나머지 표시
        for i in range(1, 4):
            block[i][0] -= block[0][0]
            block[i][1] -= block[0][1]

        ty = types.index(block[1:])
        block_by_type[tuple(block[0])] = ty

    # 블럭지우기 시작
    candidate = [2, 3, 5, 6, 8]
    while True:
        remove = []
        # 지울애들 찾기
        for start in block_by_type.keys():
            if block_by_type[start] in candidate:
                rm = True
                for check in remove_by_type[block_by_type[start]]:
                    # y축체크
                    for r in range(start[0] + check[0] +1):
                        if board[r][start[1] + check[1]]:
                            rm = False
                if rm:
                    remove.append(start)

        if not remove:
            return answer
        # 지우기
        for b in remove:
            board[b[0]][b[1]] = 0
            for drc in types[block_by_type[b]]:
                board[b[0] + drc[0]][b[1] + drc[1]] = 0
            answer +=1
            del (block_by_type[b])

print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]))