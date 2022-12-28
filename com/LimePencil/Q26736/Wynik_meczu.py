import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
a=s.count("A")
b=s.count("B")
print(f"{a} : {b}")