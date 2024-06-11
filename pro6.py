# # 6
import math
x, y = map(int, input().split())
s = x/y
print("floor {} / {} = {}".format(x, y, x//y))
print("ceil {} / {} = {}".format(x, y, math.ceil(s)))
print("round {} / {} = {}".format(x, y, round(s)))
## built in function
x, y = map(int, input().split())
s = x/y
m = s*10
c = m % 10
if(c > 0):
    s += 1
print(int(s))