import sys

input = sys.stdin.readline
arr = []
while True:
    n=int(input())
    if n==0:
        break
    arr.append(n)
m=max(arr)
is_prime=[True for _ in range(m+1)]
p=2
while (p*p <= m):
        if is_prime[p]:
            for i in range(p*p,m+1,p):
                is_prime[i] = False
        p +=1
for a in arr:
    for i in range(2,a//2+1):
        if is_prime[i] and is_prime[a-i]:
            print(f"{a} = {i} + {a-i}")
            break