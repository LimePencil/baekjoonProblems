import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    print(f"Case #{t}:",max(list(map(int,input().split()))))