import sys

s = sys.stdin.readline().rstrip("\n")
for k,c in enumerate(s):
    print(c,end="")
    if k%10 ==9:
        print()

