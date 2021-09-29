import sys

ans =""
while ((line := sys.stdin.readline().strip("\n")) != "."):
    square_bracket = 0
    round_bracket = 0
    balanced = True
    prev_open_bracket = []
    for c in line:
        if c == "[":
            square_bracket +=1
            prev_open_bracket.append(c)
        elif c == "]":
            square_bracket -=1
            if len(prev_open_bracket) == 0 or prev_open_bracket.pop() != "[":
                balanced = False
                break
        elif c == "(":
            round_bracket +=1
            prev_open_bracket.append(c)
        elif c == ")":
            round_bracket -=1
            if len(prev_open_bracket) == 0 or prev_open_bracket.pop() != "(":
                balanced = False
                break
    if(square_bracket != 0 or round_bracket !=0):
        balanced = False
    ans += ("yes" if balanced else "no") + "\n"
print(ans)
