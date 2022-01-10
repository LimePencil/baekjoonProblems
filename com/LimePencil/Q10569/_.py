import sys


t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    v, e = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    print(2+e-v)

