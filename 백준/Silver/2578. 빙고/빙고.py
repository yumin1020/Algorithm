def bingo_game(board, called_numebers):
    position = {}
    for i in range(5):
        for j in range(5):
            position[board[i][j]] = (i, j)
    
    bingo = [[False] * 5 for _ in range(5)]

    def count_bingo():
        bingo_count = 0

        # 가로
        for i in range(5):
            if all(bingo[i]):
                bingo_count += 1

        # 세로
        for j in range(5):
            if all(bingo[i][j] for i in range(5)):
                bingo_count += 1
        
        # 대각선 확인
        if all(bingo[i][i] for i in range(5)):
            bingo_count += 1
        if all(bingo[i][4-i] for i in range(5)):
            bingo_count += 1
        
        return bingo_count
    
    # 부르는 숫자 체크
    for count, num in enumerate(called_numebers, 1):
        x, y = position[num]
        bingo[x][y] = True
        if count_bingo() >= 3:
            return count
    
    return -1

board = [list(map(int, input().split())) for _ in range(5)]
called_numbers = []
for _ in range(5):
    called_numbers.extend(map(int, input().split()))
result = bingo_game(board, called_numbers)
print(result)