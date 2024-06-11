#4-F. Digits Summation##
x, y = map(int, input().split())
a = [x, y]
# a.append(x)
b = []
b = b.extend(a)
print(a)
number = 123456789
list = []
while number > 0:
    list.append(number % 10)
    number = number-number % 10
print(list)
