import sys

input = sys.stdin.readline
prev="right"
while True:
    n = input().rstrip()
    if n=="99999":
        break
    s=int(n[0])+int(n[1])
    if s==0:
        print(prev,n[2:])
    elif s%2==0:
        print(f"right {n[2:]}")
        prev="right"
    else:
        print(f"left {n[2:]}")
        prev="left"