# check explanation at readme.md, where i explain logic and perfectNumber function
import random

def power(x, y, p):
    r = 1
    x = x % p
    while y > 0:
        if y & 1:
            r = (r * x) % p
        y = y >> 1
        x = (x * x) % p
    return r

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def isPrime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miillerTest(d, n):
            return False
    return True

def perfectNumber(n):
    m = int(n * 0.5)
    if isPrime(n-m) and isPrime(2**(n-m) - 1):
        r = (2**n) - (2**m)
        return True, r
    else:
        return False

if __name__ == "__main__":
    k = 5 # ammount of miller tests
    i = 3
    open("perfects.txt", "w")
    while True:
        result = perfectNumber(i)
        if result:
            print(result)
            open("perfects.txt", "a+").write(f"{result[1]}\n")
        i += 2
