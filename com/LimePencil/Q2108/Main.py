import sys
import statistics

n = int(sys.stdin.readline())

list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
print(round(statistics.mean(list)))
print(statistics.median(list))
mode = statistics.multimode(list)
mode.sort()
print(mode[1] if len(mode) > 1 else mode[0])
print(max(list) - min(list))