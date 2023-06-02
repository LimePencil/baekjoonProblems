import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
x=0
for _ in range(n):
    row=list(map(int,input().split()))
    prev_grundy=0
    for i in range(m-1,-1,-1):
        if i==m-1:
            prev_grundy=row[i]
        else:
            if prev_grundy<=row[i]-1:
                prev_grundy=row[i]
            else:
                prev_grundy=row[i]-1
    x^=prev_grundy    
print("koosaga" if x else "cubelover")