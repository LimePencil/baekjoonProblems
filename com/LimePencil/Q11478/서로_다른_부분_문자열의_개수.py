import sys

input = sys.stdin.readline
num=set()
s=input().rstrip()
for i in range(len(s)):
    st=""
    for j in range(i,len(s)):
        st+=s[j]
        num.add(st)
print(len(num))