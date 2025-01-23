def has_unique_digits(number):
    num_str = str(number)
    return len(num_str) == len(set(num_str))

def count_unique_numbers(n, m):
    count = 0
    for num in range(n, m + 1):
        if has_unique_digits(num):
            count += 1
    return count

import sys
input = sys.stdin.read
data = input().strip().split("\n")

results = []
for line in data:
    n, m = map(int, line.split())
    results.append(count_unique_numbers(n, m))

print("\n".join(map(str, results)))