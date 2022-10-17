import sys

input = lambda: sys.stdin.readline().rstrip()
s=input()
if len(s)==s.count("I")+s.count("O")+s.count("S")+s.count("H")+s.count("Z")+s.count("X")+s.count("N"):
    print("YES")
else:
    print("NO")