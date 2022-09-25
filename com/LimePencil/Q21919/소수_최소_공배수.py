import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(set(map(int,input().split())))
m=1000000
is_prime=[True for _ in range(m+1)]
p=2
while (p*p <= m):
        if is_prime[p]:
            for i in range(p*p,m+1,p):
                is_prime[i] = False
        p +=1
ans=1
for a in arr:
    if is_prime[a]:
        ans*=a

print(ans if ans!=1 else -1)