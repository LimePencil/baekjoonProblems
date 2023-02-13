import sys
import statistics

input = lambda: sys.stdin.readline().rstrip()
cnt=0
while True:
    cnt+=1
    arr = list(map(int,input().split()))
    if arr==[0]:
        break
    if arr[0]%2==1:
        print(f"Case {cnt}: {arr[1+arr[0]//2]:.1f}")
    else:
        print(f"Case {cnt}: {(arr[arr[0]//2]+arr[1+arr[0]//2])/2:.1f}")