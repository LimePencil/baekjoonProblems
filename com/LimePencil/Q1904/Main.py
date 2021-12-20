import sys

def fib(n):
    a = 1
    b = 2
    for i in range(n-1):
        temp  = a
        a = b
        b = (temp+b)%15746
    return a
        
n = int(sys.stdin.readline().rstrip("\n"))
ans = fib(n)
print(ans%15746)