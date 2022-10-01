import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
equation=[list(map(int,input().split())) for _ in range(m)]
for i in range(1<<n):
    b=('{:0'+str(n)+'b}').format(i)
    found=True
    for x,y in equation:
        if x>0 and y>0 and b[abs(x)-1]=='0' and b[abs(y)-1]=='0':
            found=False
            break
        elif x>0 and y<0 and b[abs(x)-1]=='0' and b[abs(y)-1]=='1':
            found=False
            break
        elif x<0 and y>0 and b[abs(x)-1]=='1' and b[abs(y)-1]=='0':
            found=False
            break
        elif x<0 and y<0 and b[abs(x)-1]=='1' and b[abs(y)-1]=='1':
            found=False
            break
    if found:
        print(1)
        exit()
print(0)