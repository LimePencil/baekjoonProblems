# KMP Algorithm

import sys
n = int(sys.stdin.readline().strip("\n"))
m = int(sys.stdin.readline().strip("\n"))
s = sys.stdin.readline().strip("\n")
pn = "IO"*n+"I"
count = 0


def findPattern(s,pn):
    global count
    lps = LPS_table(pn)
    i = 0
    j = 0
    while i<len(s):
        if s[i] == pn[j]:
            i+=1
            j+=1
        elif s[i] != pn[j]:
            if j !=0:
                j = lps[j-1]
            else:
                i+=1
        if j == len(pn):
            j = lps[j-1]
            count +=1
        

def LPS_table(pn):
    lps = [0]*len(pn)
    length = 0
    i = 1
    while i < len(lps):
        if pn[i] ==  pn[length]:
            length +=1
            lps[i] = length
            i+= 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1
    return lps

findPattern(s,pn)
print(count)