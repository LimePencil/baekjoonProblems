import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()
submarine=True
if s[-1]=="0":
    submarine=False
else:
    new_s=""
    for i in range(len(s)):
        if i>=2 and s[i-2:i+1]=="000":
            continue
        new_s+=s[i]
    s=new_s
    
    while len(s)>0:
        if len(s)>=2 and s[0:2]=="01":
            s=s[2:]
        elif len(s)>=4 and s[0:4]=="1001":
            s=s[4:]
            while len(s)>=4 and s[0:4]=="1001":
                s=s[4:]
            while len(s)>0 and s[0]=="1":
                s=s[1:]
        else:
            submarine=False
            break
print("SUBMARINE" if submarine else "NOISE")
