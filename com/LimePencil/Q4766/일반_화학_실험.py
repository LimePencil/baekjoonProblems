import sys

input = sys.stdin.readline
n = []
while True:
    x=float(input())
    if x==999:
        break
    n.append(x)
for i in range(len(n)-1):
    print("{:.2f}".format(n[i+1]-n[i]))