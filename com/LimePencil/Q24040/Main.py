import sys

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip("\n"))
    if n%3==2 or n%9 ==0:
        print("TAK")
    else:
        print("NIE")