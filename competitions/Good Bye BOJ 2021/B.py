# TLE

import sys
import random

sys.setrecursionlimit(10**4)


def power(x : int, y : int, p : int) -> int:
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x*x) % p
    return res


def gcd(a : int, b : int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def miller_rabin(n : int, a : int) -> bool:
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d//2

    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for _ in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False


def is_prime(n : int) -> bool:
    alist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    for a in alist:
        if n == a:
            return True
            
        if not miller_rabin(n, a):
            return False
    return True


def pollardRho(n : int) -> int:

    if n == 1:
        return 1

    if n % 2 == 0:
        return 2
    if n%3 ==0:
        return 3
    if n%5 ==0:
        return 5

    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1

    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)

        if d == n:
            return pollardRho(n)
    if is_prime(d):
        return d
    else:
        return pollardRho(d)

t= int(sys.stdin.readline().rstrip("\n"))
c = []
for _ in range(t):

    i= int(sys.stdin.readline().rstrip("\n"))
    ans = "NIE"
    temp = i 
    found = False
    while not found  and temp>1:
        if not is_prime(temp):
            a = pollardRho(temp)
        else:
            a = temp
        temptemp = temp
        while temptemp%a == 0:
            temptemp//=a
            if (a+i//a)%3 == 0:
                ans = "TAK"
                found = True
                break
        temp = temptemp
    c.append(ans)
print("\n".join(c))