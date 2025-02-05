import bisect

def paint_tiles(N, A, B):
    result = [0] * N
    
    for i in range(N):
        j = bisect.bisect_right(B, A[i])
        result[i] = j - i - 1
    return result

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*paint_tiles(N, A, B))
