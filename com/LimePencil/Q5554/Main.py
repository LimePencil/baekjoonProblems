import sys

total = 0
for _ in range(4):
    total += int(sys.stdin.readline().rstrip("\n"))
print(total//60)
print(total%60)