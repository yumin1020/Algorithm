import sys

def backtrack(arr, path, start, M):
    if len(path) == M:
        print(*path)
        return
    for i in range(start, len(arr)):
        backtrack(arr, path + [arr[i]], i + 1, M)

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(map(int, sys.stdin.readline().split()))

backtrack(numbers, [], 0, M)