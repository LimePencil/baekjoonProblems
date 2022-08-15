import sys

input = sys.stdin.readline
for i in range(1,int(input())+1):
    print(f"Case {i}:")
    n=int(input())
    for j in range(1,n//2+1):
        if n-j <=6:
            print(f"({j},{n-j})")