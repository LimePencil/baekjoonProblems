s=input()

y=list("YONSEI")
k=list("KOREA")
for c in s:
    if c==y[0]:
        y.pop(0)
    if c==k[0]:
        k.pop(0)
    if len(y)==0:
        print("YONSEI")
        break
    if len(k)==0:
        print("KOREA")
        break