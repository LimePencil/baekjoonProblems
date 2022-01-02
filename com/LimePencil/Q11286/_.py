from queue import PriorityQueue
import sys

q= PriorityQueue()
for i in range(int(sys.stdin.readline().rstrip("\n"))):
    n = int(sys.stdin.readline().rstrip("\n"))
    if(n != 0):
        q.put((abs(n),n))
    elif n==0 and q.empty() == False:
        a = q.get()
        sys.stdout.write(str(a[1]) + "\n")
    else:
        sys.stdout.write("0\n")