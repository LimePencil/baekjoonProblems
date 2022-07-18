import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    s=sum(list(map(int,input().split())))
    print("Equilibrium" if s==0 else ("Left" if s<0 else "Right"))