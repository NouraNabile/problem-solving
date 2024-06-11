# #15##The last 2 digits
x, y, z, s = map(int, input().split())
m = x*y*z*s
print(m % 100)

#16##Hard Compare
# x, y, z, s = map(int, input().split())
#if(x**y > z**s):
    #print("yes")
#else:
print("no")
import math
x, y, z, s = map(int, input().split())
if(y*math.log(x) > s*math.log(z)):
    print("YES")
else:
    print("NO")