import sys

def get_cuts(arr,cut):
    total = 0
    for i in arr:
        total += max(0,i//cut)
    return total
def binary_search(arr,low, high, target):
    mid = 0
    while(low+1<high):
        mid = (low + high)//2
        cables_cut = get_cuts(arr,mid)
        param = target<=cables_cut
        if param:
            low = mid
        else:
            high = mid
    return low

n, m = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
cables = []
for _ in range(n):
    cables.append(int(sys.stdin.readline().rstrip("\n")))
cables.sort()
print(binary_search(cables,0,cables[-1]+1,m))
