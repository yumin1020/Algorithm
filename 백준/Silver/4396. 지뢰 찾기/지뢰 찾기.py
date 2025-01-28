def count_mines(x, y, n, map1, dx, dy):
    count = 0
    for i in range(8):  # 8방향 확인
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and map1[nx][ny] == '*':
            count += 1
    return count

def my_func():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # 격자 크기, 지뢰 지도, 플레이어 지도
    n = int(data[0])
    map1 = data[1:n+1]
    map2 = data[n+1:2*n+1]
    result = [['.'] * n for _ in range(n)]
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    game_over = False

    # 격자 탐색
    for i in range(n):
        for j in range(n):
            if map2[i][j] == 'x':  # 플레이어가 연 칸
                if map1[i][j] == '*':  # 지뢰를 연 경우
                    game_over = True
                else:  # 지뢰가 없는 칸
                    result[i][j] = str(count_mines(i, j, n, map1, dx, dy))

    # 게임 오버 시 모든 지뢰 표시
    if game_over:
        for i in range(n):
            for j in range(n):
                if map1[i][j] == '*':
                    result[i][j] = '*'

    # 결과 출력
    for row in result:
        print(''.join(row))

my_func()
