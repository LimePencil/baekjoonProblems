import sys

input = lambda: sys.stdin.readline().rstrip()
for t in range(1, int(input())+1):
    n = int(input())
    s=input()
    n+=s.count('c')
    n-=s.count('b')
    print(f"Data Set {t}:")
    print((n))
    print()