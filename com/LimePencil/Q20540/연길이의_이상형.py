import sys

input = sys.stdin.readline
s=input().rstrip()
new_s=""
if s[0]=="E":
    new_s+="I"
else:
    new_s+="E"

if s[1]=="S":
    new_s+="N"
else:
    new_s+="S"

if s[2]=="T":
    new_s+="F"
else:
    new_s+="T"

if s[3]=="J":
    new_s+="P"
else:
    new_s+="J"
print(new_s)