import sys

def mex(p):
    if len(p)==0:
        return 0
    for i in range(len(p)):
        if i != p[i]:
            return i
    return len(p)

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
grundy=[0]*(n+1)
grundy[1]=1
grundy[2]=1
grundy[3]=1
for i in range(4,n+1):
    s=set()
    for j in range(i):
        l_partition=j
        r_partition=i-j-1
        l_grundy=grundy[max(0,l_partition-2)]
        r_grundy=grundy[max(0,r_partition-2)]
        s.add(l_grundy^r_grundy)
    grundy[i]=mex(sorted(s))
print(1 if grundy[n]!=0 else 2)