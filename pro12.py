#12#O. Calculator#
x = input()
y = x[2]
z = x[1]
x = x[0]
if(z == '+'):
    print(int(x)+int(y))
elif(z == '-'):
    print(int(x)-int(y))
elif(z == '*'):
    print(int(x)*int(y))
elif(z == '/'):
    print(int(x)/int(y))