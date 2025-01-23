import math

def equal_f(s, t):
    len_s, len_t = len(s), len(t)
    lcm_length = (len_s  * len_t) // math.gcd(len_s, len_t)

    expanded_s = s * (lcm_length // len_s)
    expanded_t = t * (lcm_length // len_t)

    return 1 if expanded_s == expanded_t else 0

s = input()
t = input()

print(equal_f(s, t))