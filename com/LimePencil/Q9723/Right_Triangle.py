import sys

input = sys.stdin.readline
for t in range(1,int(input())+1):
    a,b,c=sorted(list(map(int,input().split())))
    d="YES" if a**2+b**2==c**2 else "NO"
    print(f"Case #{t}: {d}")