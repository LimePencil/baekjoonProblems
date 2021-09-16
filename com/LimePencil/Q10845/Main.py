from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque()
st = []
for i in range(n):
    a = sys.stdin.readline().strip('\n').rstrip().split(" ")
    if(a[0] == "push"):
        stack.append(int(a[1]))
    elif(a[0] == "back"):
        if(len(stack) != 0):
            st.append(stack[-1])
        else:
            st.append("-1") 
    elif(a[0] == "front"):
        if(len(stack) != 0):
            st.append(stack[0])
        else:
            st.append("-1") 
    elif(a[0] == "size"):
        st.append(len(stack))
    elif(a[0] == "pop"):
        if(len(stack) == 0):
            st.append("-1")
        else:
            st.append(stack.popleft())
    elif(a[0] == "empty"):
        if(len(stack) != 0):
            st.append("0")
        else:
            st.append("1")

ans = ""
for i in st:
    ans += str(i) + '\n'
sys.stdout.write(ans)