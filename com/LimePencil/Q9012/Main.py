n = int(input())
for i in range(n):
    sentence = input()
    VPS = True
    count = 0
    for w in sentence:
        if w == '(':
            count +=1
        elif w ==')':
            count -=1
        if count <0:
            VPS = False
            break
    if count != 0:
        VPS = False
    if VPS:
        print("YES")
    else:
        print("NO")
