def min_flips(S):
    # 카운트 초기화
    count0 = 0
    count1 = 0

    if S[0] == '0':
        count0 += 1
    else:
        count1 += 1
    
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            if S[i] == '0':
                count0 += 1
            else:
                count1 += 1
    
    return min(count0, count1)


S = input()
print(min_flips(S))