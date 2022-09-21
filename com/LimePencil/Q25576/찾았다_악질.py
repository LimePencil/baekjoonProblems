import sys

input = lambda: sys.stdin.readline().rstrip()
n,m = list(map(int,input().split()))
lalpa=list(map(int,input().split()))
cnt=0
for _ in range(n-1):
    arr=list(map(int,input().split()))
    diff=sum(abs(lalpa[i]-arr[i]) for i in range(m))
    if diff>2000:
        cnt+=1
if cnt>=(n-1)/2:
    print("YES")
else:
    print("NO")