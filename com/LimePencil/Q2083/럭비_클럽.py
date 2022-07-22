import sys

input = sys.stdin.readline
while True:
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    if a=="#":
        break
    print(a,"Senior" if b>17 or c>=80 else "Junior")