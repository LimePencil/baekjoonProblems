import sys

input = sys.stdin.readline
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    print("Scenario #{}:".format(i+1))
    print((m*(m+1)-n*(n-1))//2)
    print()