n, m = map(int, input().split())

def cal_gcd(n, m):
    gcd = 1
    small_value = n if n < m else m 
    
    for i in range(2, small_value + 1):
        if (n % i == 0) and (m % i == 0) == True:
            gcd = i
    return gcd;

def lcm(i, j):
    gcd_val = cal_gcd(n, m)
    result = 1
    i = i // gcd_val
    j = j // gcd_val
    result = i * j * gcd_val
    return result

print(lcm(n, m))

