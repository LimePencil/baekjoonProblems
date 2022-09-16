import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s = input().rstrip()
    ans=0
    for c in s:
        if c==" ":
            continue
        ans+=ord(c)-64
    if ans==100:
        print("PERFECT LIFE")
    else:
        print(ans)