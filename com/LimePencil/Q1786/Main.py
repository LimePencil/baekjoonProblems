# KMP Algorithm

import sys
s = sys.stdin.readline().rstrip("\n")
pn = sys.stdin.readline().rstrip("\n")

count  = 0
result = []
def findPattern(s,pn):
    global count, ans
    lps = LPS_table(pn)
    i = 0
    j = 0
    l_s = len(s)
    l_p = len(pn)
    for i in range(l_s):
        while(j >0 and s[i] != pn[j]):
            j = lps[j-1]
        if s[i] == pn[j]:
            j+=1
            if j == l_p:
                # when found 
                count +=1
                result.append(str(i-j+2))
                j = lps[j-1]
                
def LPS_table(pn):
    lps = [0]*len(pn)
    length = 0
    for i in range(1,len(pn)):      
        while length > 0 and pn[i] != pn[length]:
            length = lps[length-1]
        if pn[i] == pn[length]:
            length +=1
            lps[i] = length
    return lps

findPattern(s,pn)
print(str(count))
print(*result)