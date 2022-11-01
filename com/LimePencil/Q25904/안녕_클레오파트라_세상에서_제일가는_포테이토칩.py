import sys

input = lambda: sys.stdin.readline().rstrip()
n,x = list(map(int,input().split()))
people=list(map(int,input().split()))
for i in range(300):
    if people[i%n]<i+x:
        print(i%n+1)
        break
