import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
X = int(data[1])
A = map(int, data[2:])

print(" ".join(str(num) for num in A if num < X))