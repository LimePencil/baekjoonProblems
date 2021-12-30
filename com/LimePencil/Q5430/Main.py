import sys
from collections import deque

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    command = sys.stdin.readline().rstrip("\n")
    n = int(sys.stdin.readline().rstrip("\n"))
    st = sys.stdin.readline().rstrip("\n").rstrip("]").strip("[")
    arr = []
    if st != "":
        arr = list(map(int,st.split(",")))
    reversed = False
    d = deque(arr)
    ans = []
    for i in command:
        if i == "R":
            reversed = not reversed
        else:
            if len(d) >0:
                if reversed:
                    d.pop()
                else:
                    d.popleft()
            else:
                print("error")
                ans = -1
                break
    if ans!= -1:
        if reversed:
            d.reverse()
            ans = list(d)
        else:
            ans = list(d)
        print("["+",".join([str(i) for i in ans])+"]")

