import sys

input = lambda: sys.stdin.readline().rstrip()

def mex(p):
    for o in range(len(p)):
        if o!=p[o]:
            return o
    return len(p)


grundy_single=[[0]*101 for _ in range(101)]

for i in range(1,101):
    for j in range(i+1):
        s=set()
        # check diagonal
        for k in range(1,j+1):
            s.add(grundy_single[i-k][j-k]) 
        # check horizontal
        for k in range(1,i+1):
            s.add(grundy_single[i-k][j])
        # check vertical
        for k in range(1,j+1):
            s.add(grundy_single[i][j-k])
        x=mex(sorted(s))
        grundy_single[i][j]=x
        grundy_single[j][i]=x

grundy_double=[[0]*101 for _ in range(101)]

for i in range(1,101):
    for j in range(1,i):
        if grundy_single[i][j]==0:
            grundy_double[i][j]=0
            grundy_double[j][i]=0
            continue
        s=set()
        # check diagonal
        for k in range(1,j+1):
            s.add(grundy_double[i-k][j-k]) 
        # check horizontadk
        for k in range(1,i+1):
            s.add(grundy_double[i-k][j])
        # check vertical
        for k in range(1,j+1):
            s.add(grundy_double[i][j-k])
        x=mex(sorted(s))
        grundy_double[i][j]=x
        grundy_double[j][i]=x
n = int(input())
c=0
has_zero=False
for _ in range(n):
    x,y=list(map(int,input().split()))
    if x==0 or y==0 or x==y:
        has_zero=True
    if n==1:
        c^=grundy_single[x][y]
    else:
        c^=grundy_double[x][y]
print("Y" if c or has_zero else "N")
