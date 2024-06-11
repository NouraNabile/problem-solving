# 1-Simple Calculator##
x, y = map(int, input("").split())
sum = x+y
mul = x*y
sub = x-y
# print(f"{x}+"+"+"{y}"={sum})
print("{} + {} = {}".format(x, y, sum))
print("{} * {} = {}".format(x, y, mul))
print("{} - {} = {}".format(x, y, sub))