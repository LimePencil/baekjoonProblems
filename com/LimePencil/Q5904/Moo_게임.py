import sys
import bisect

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
arr=[3]
for i in range(1,31):
    arr.append(arr[i-1]*2+i+3)
idx=bisect.bisect_left(arr,n)
n-=1
for i in range(idx,-1,-1):
    if i==0:
        print("moo"[n])
        break
    if n<arr[i-1]:
        pass
    elif arr[i-1]<=n<=arr[i-1]+i+2:
        print(("m"+"o"*(i+2))[n-arr[i-1]])
        break
    else:
        n-=arr[i-1]+i+3