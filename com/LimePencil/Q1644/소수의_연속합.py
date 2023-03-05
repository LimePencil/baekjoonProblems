import sys

input = lambda: sys.stdin.readline().rstrip()

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    l=[]
    for i in range(2,len(prime)):
        if prime[i]:
            l.append(i)
    return l
n = int(input())
p=SieveOfEratosthenes(n)
sum_p=[0]*(len(p)+1)
sum_p[0]=0
for i in range(1,len(p)+1):
    sum_p[i]=sum_p[i-1]+p[i-1]
cnt=0
for i in range(1,len(p)+1):
    s=1
    e=len(p)-i+1
    while s<=e:
        m=(s+e)//2
        x=sum_p[m+i-1]-sum_p[m-1]
        if x==n:
            cnt+=1
            break
        elif x<n:
            s=m+1
        else:
            e=m-1
print(cnt)