import sys
import math


n = int(sys.stdin.readline())
ans = 4
n1 = math.sqrt(n)
if (float.is_integer(n1)):
    ans = 1 
else:
    for n2 in range(1, math.floor(n1)+1):
        if(float.is_integer(math.sqrt(n-n2**2))):
            ans = 2
    if ans != 2:
        for n2 in range(1,math.floor(n1)+1):
            for n3 in range(1,math.floor(math.sqrt(n-n2**2))+1):
                if(float.is_integer(math.sqrt(n-n2**2-n3**2))):
                    ans = 3

sys.stdout.write(str(ans))