ls = list(map(int,input().split(" ")))
ascending = True
descending = True
prev = 0
for i in range(len(ls)):
    curr = ls[i]
    if(i == 0):
        pass
    elif(i == 1):
        if(curr > prev):
            descending = False
        else:
            ascending = False
    else:
        if(ascending and (curr < prev)):
            ascending = False
            break
        elif(descending and (curr > prev)):
            descending = False
            break
    prev = curr
ans = ""
if(ascending):
    ans = "ascending"
elif(descending):
    ans = "descending"
else:
    ans = "mixed"
print(ans)
    
