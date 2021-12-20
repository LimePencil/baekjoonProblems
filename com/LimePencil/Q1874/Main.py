from collections import deque
import sys

n = int(sys.stdin.readline().rstrip("\n"))
final_stack = []
stack = deque()
ans = []
ans_write = []
for _ in range(n):
    final_stack.append(int(sys.stdin.readline().rstrip("\n")))
num_used = 0
for i in final_stack:
    while(i>num_used):
        num_used +=1
        stack.append(num_used)
        ans_write.append("+")
    if(i == stack[-1]):
        a= stack.pop()
        ans.append(a)
        ans_write.append("-")
if(ans == final_stack):
    sys.stdout.write('\n'.join(ans_write))
else:
    sys.stdout.write("NO")