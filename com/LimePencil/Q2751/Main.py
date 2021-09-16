import sys
n = int(sys.stdin.readline().strip('\n'))
list = []
for i in range(n):
    list.append(int(sys.stdin.readline().strip('\n')))
list.sort()
ans = ""
for e in list:
    ans += str(e) + "\n"
sys.stdout.write(ans)