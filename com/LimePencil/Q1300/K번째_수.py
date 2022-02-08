import sys

n = int(sys.stdin.readline().rstrip("\n"))
k = int(sys.stdin.readline().rstrip("\n"))

low  = 0
high = k
ans = 0
while low<=high:
    mid = (low+high)//2
    count = 0
    for i in range(1,n+1):
        count+=min(n,mid//i)
    if count <k:
        low = mid+1
    else:
        high = mid-1
        ans = mid
print(ans)