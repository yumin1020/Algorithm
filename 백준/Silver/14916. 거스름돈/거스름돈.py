def minimum_coins(n):
    five_coin_count = n // 5
    remainder = n % 5

    while five_coin_count >= 0:
        if remainder % 2 == 0:
            two_coin_count = remainder // 2
            return five_coin_count + two_coin_count
        
        five_coin_count -= 1
        remainder += 5
    
    return -1

n = int(input())
print(minimum_coins(n))
