while True:
    n = input()
    if n =="0":
        break
    l = 1
    for s in n:
        if s =="1":
            l+=3
        elif s=="0":
            l+=5
        else:
            l+=4
    print(l)