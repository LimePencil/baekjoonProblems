import sys

input = lambda: sys.stdin.readline().rstrip()

def dec_to_base(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        base_num += str(dig)
        num //= base
    base_num = base_num[::-1]
    return base_num

n = int(input())
ans=0
for i in range(2,11):
    s=dec_to_base(n,i)
    if s==s[::-1]:
        ans+=1
        print(i,s)
if ans==0:
    print("NIE")