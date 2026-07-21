n, m = map(int, input().split())

def gcd(n, m):
    gcd = 1
    flag = False
    small_value = n if n < m else m 
    
    for i in range(2, small_value + 1):
        if (n % i == 0) and (m % i == 0) == True:
            flag = True
            gcd = i
        else:
            flag = False

    print(gcd)

gcd(n, m)