import sys

n, m = list(map(int,sys.stdin.readline().strip('\n').split(" ")))
ls = []
dt = {}
ans = ""
for i in range(n):
    name = sys.stdin.readline().strip('\n')
    ls.append(name)
    dt[name] = i+1
for j in range(m):
    question = sys.stdin.readline().strip('\n')
    if question.isdigit():
        ans += ls[int(question)-1] + "\n"
    else:
        ans += str(dt[question]) + "\n"

sys.stdout.write(ans)