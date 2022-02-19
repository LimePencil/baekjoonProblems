import sys

a = int(sys.stdin.readline().rstrip("\n"))
b = int(sys.stdin.readline().rstrip("\n"))
c = int(sys.stdin.readline().rstrip("\n"))
d = int(sys.stdin.readline().rstrip("\n"))
e = int(sys.stdin.readline().rstrip("\n"))
print(min(a,b,c)+min(d,e)-50)