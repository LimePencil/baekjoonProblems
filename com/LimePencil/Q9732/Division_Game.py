import sys


input = lambda: sys.stdin.readline().rstrip()

exp=[0]*10001
sieve=[True]*10001
primes=[]
for i in range(2,10001):
    if sieve[i]:
        primes.append(i)
        for j in range(i,10001,i):
            sieve[j]=False
exp=[0]*10001
for i in range(2,10001):
    j=i
    cnt=0
    for p in primes:
        while j%p==0:
            cnt+=1
            j//=p
    exp[i]=cnt
for t in range(1,int(input())+1):
    n,m=list(map(int,input().split()))
    x=0
    for _ in range(n):
        x^=sum(map(lambda x: exp[x], list(map(int,input().split()))))

    print(f"Case #{t}: {'YES' if x else 'NO'}")
