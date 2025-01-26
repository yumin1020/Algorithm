s = input().strip()
A = [s[i:] for i in range(len(s))]
A.sort()

for a in A:
    print(a)