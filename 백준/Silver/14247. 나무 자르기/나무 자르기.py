def cut_tree(n, H, A):
    trees = sorted(zip(A, H))

    total_wood = 0
    for day, (growth, height) in enumerate(trees):
        total_wood += height + (day * growth)

    return total_wood

# 입력 처리
n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

print(cut_tree(n, H, A))