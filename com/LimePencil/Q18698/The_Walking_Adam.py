import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s=input()
    n=0
    for c in s:
        if c=="U":
            n+=1
        else:
            break
    print(n)