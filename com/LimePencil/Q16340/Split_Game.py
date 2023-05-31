import sys

def mex(p):
    for i in range(len(p)):
        if i!=p[i]:
            return i
    else:
        return len(p)

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
p = list(map(int,input().split()))

grundy=[0]*2001
for i in range(2,2001):
    s=set()
    for k in range(1,i):
        t=(0 if (i//k)%2==0 else grundy[k])^(grundy[i%k])
        s.add(t)
    grundy[i]=mex(sorted(list(s)))
x=0
for e in p:
    x^=grundy[e]
if x!=0:
    print("First")
else:
    print("Second")