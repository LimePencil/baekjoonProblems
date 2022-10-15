import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s=input()
num_s=s.count('s')
num_t=s.count('t')
while num_s!=num_t:
    s=s[1:]
    num_s=s.count('s')
    num_t=s.count('t')
print(s)