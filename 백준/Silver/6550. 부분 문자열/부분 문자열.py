def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

import sys
input = sys.stdin.read
data = input().strip().split('\n')

for line in data:
    s, t = line.split()
    if is_subsequence(s, t):
        print("Yes")
    else:
        print("No")

