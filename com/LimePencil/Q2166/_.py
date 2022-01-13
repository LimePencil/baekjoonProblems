import sys
import math

n = int(sys.stdin.readline().rstrip("\n"))
points = []
x_mid = 0
y_mid = 0
for _ in range(n):
    x,y = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    x_mid += x
    y_mid += y
    points.append([x,y,0])
x_mid /= n
y_mid /= n

# for p in points:
#     sin = (p[1]-y_mid)/math.dist(p[:2],[x_mid,y_mid])
#     delta_x = p[0]-x_mid
#     if sin >=0:
#         if delta_x >= 0:
#             p[2] = math.asin(sin)
#         else:
#             p[2] = math.pi - math.asin(sin)
#     else:
#         if delta_x >= 0:
#             p[2] = 2*math.pi - math.asin(-sin)
#         else:
#             p[2] = math.pi + math.asin(-sin)
# points.sort(key= lambda x : x[2])
a= 0
b=0
for i in range(n):
    a += points[i][0]*points[(i+1)%n][1]
    b += points[(i+1)%n][0]*points[i][1]
print(round(abs(a-b)/2,1))