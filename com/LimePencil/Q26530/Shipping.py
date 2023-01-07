import sys

input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n = int(input())
    ans=0
    for i in range(n):
        arr = input().split()
        ans+=int(arr[1])*float(arr[2])
    print(f"${ans:.2f}")