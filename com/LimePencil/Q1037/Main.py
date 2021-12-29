import sys

n = int(sys.stdin.readline().rstrip("\n"))

q = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
q.sort()
print(q[0]*q[-1])