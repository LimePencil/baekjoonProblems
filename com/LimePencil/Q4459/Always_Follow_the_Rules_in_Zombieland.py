import sys

input = sys.stdin.readline
m=int(input())
rule=[input().rstrip() for _ in range(m)]
for _ in range(int(input())):
    n=int(input())
    if 0<n<=m:
        print(f"Rule {n}: {rule[n-1]}")
    else:
        print(f"Rule {n}: No such rule")
