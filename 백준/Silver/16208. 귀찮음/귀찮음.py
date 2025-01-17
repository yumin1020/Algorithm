def minimum_cut_cost(n, lengths):
    total_cost = 0

    while len(lengths) > 1:
        lengths.sort()
        
        first = lengths.pop(0)
        second = lengths.pop(0)
        
        cost = first * second
        total_cost += cost
        
        lengths.append(first + second)
    
    return total_cost


n = int(input())
lengths = list(map(int, input().split()))
print(minimum_cut_cost(n, lengths))
