import sys

input = sys.stdin.readline
n,t= list(map(int,input().split()))
arr = list(map(int,input().split()))
done=0
for i in range(n+1):
    if i==n:
        print(n)
        break
    done+=arr[i]
    if done>t:
        print(i)
        break