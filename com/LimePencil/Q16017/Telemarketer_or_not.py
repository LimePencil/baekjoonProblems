import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a==8 or a==9)and(d==8 or d==9)and b==c:
    print("ignore")
else:
    print("answer")