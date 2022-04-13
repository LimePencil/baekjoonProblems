import sys

input = sys.stdin.readline
s=input().rstrip('/n')
idx=0
found=True
for i in "UCPC":
    j=s[idx:].find(i)
    if j==-1:
        found=False
        break
    else:
        idx+=j
print("I love UCPC" if found else "I hate UCPC")