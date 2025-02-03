def spiral_matrix(N):
    matrix = [[0] * N for _ in range(N)]  # 빈 배열 생성
    y, x = N // 2, N // 2  # 시작점 (중앙)
    num = 1  # 시작 숫자

    # 반시계 방향 (위 → 오른 → 아래 → 왼)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    step = 1
    current_dir = 0

    while num <= N * N:
        for _ in range(2):  # step 크기를 2번 적용
            for _ in range(step):
                if num > N * N:
                    break

                matrix[y][x] = num  # 현재 위치에 숫자 채우기
                num += 1

                # 이동 방향 적용 (y 먼저, x 나중)
                dy, dx = directions[current_dir] 
                y, x = y + dy, x + dx  # (y, x) 형태로 이동

            current_dir = (current_dir + 1) % 4  # 방향 변경

        step += 1  # 이동 거리 증가

    return matrix

def find_position(matrix, N, target):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == target:
                return i + 1, j + 1  # 1-based index로 변환

# 입력 받기
N = int(input())
target = int(input())

# 달팽이 배열 생성
matrix = spiral_matrix(N)

# 결과 출력
for row in matrix:
    print(" ".join(map(str, row)))

# 좌표 찾기 및 출력
x, y = find_position(matrix, N, target)
print(x, y)
