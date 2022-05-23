import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c= list(map(int,input().split()))
    if a+2*b<c or (a==0 and c%2==1):
        print("NO")
    else:
        print("YES")