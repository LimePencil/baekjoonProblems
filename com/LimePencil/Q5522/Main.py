import sys

total = 0
for _ in range(5):
    total += int(sys.stdin.readline().rstrip("\n"))
print(total)