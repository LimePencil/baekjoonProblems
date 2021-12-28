import sys
import re

equation = sys.stdin.readline().rstrip("\n")
signs = []
total = 0
for i in equation:
    if i == "+" or i== "-":
        signs.append(i)

equation = list(map(int,re.split('\+|\-',equation)))
index=0
was_negative = False
for k,a in enumerate(equation):
    if k ==0:
        total += a
    else:
        s = signs[index]
        if s == "+":
            if not was_negative:
                total += a
            else:
                total -=a
        elif s== "-":
            was_negative = True
            total -=a
        index +=1
print(total)

