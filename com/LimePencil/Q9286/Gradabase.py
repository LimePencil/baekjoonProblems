import sys

input = sys.stdin.readline
for t in range(int(input())):
    print(f"Case {t+1}:")
    for _ in range(int(input())):
        n=int(input())
        if n==6:
            continue
        else:
            print(n+1)