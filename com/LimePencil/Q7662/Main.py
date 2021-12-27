import heapq
import sys
t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    list_min = []
    list_max = []
    n = int(sys.stdin.readline().rstrip("\n"))
    visited = [False]*n
    for i in range(n):  
        l= sys.stdin.readline().rstrip("\n").split(" ")
        l[1] = int(l[1])
        if l[0] == "I":
            heapq.heappush(list_min,(l[1],i))
            heapq.heappush(list_max,(-l[1],i))
            visited[i] = True
        elif l[1] == -1:
            while list_min and not visited[list_min[0][1]]:
                heapq.heappop(list_min)
            if list_min:
                visited[list_min[0][1]] = False
                heapq.heappop(list_min)
        else:
            while list_max and not visited[list_max[0][1]]:
                heapq.heappop(list_max)
            if list_max:
                visited[list_max[0][1]] = False
                heapq.heappop(list_max)
        while list_max and not visited[list_max[0][1]]:
            heapq.heappop(list_max)
        while list_min and not visited[list_min[0][1]]:
            heapq.heappop(list_min)
    if len(list_min) == 0:
        print("EMPTY")
    else:
        print(str(-1*list_max[0][0]) + " "+ str(list_min[0][0]))

# failed one
# t = int(sys.stdin.readline().rstrip("\n"))
# for _ in range(t):
#     lis = []
#     n = int(sys.stdin.readline().rstrip("\n"))
#     for _ in range(n):  
#         l= sys.stdin.readline().rstrip("\n").split(" ")
#         l[1] = int(l[1])
#         if l[0] == "I":
#             bisect.insort(lis,l[1])
#         else:
#             if len(lis) !=0:
#                 if l[-1] == -1:
#                     lis.pop(0)
#                 else:
#                     lis.pop(-1)
#     if len(lis) == 0:
#         print("EMPTY")
#     else:
#         print(str(lis[-1]) + " "+ str(lis[0]))