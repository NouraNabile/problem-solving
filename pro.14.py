# #14##Comparison
x, z, y = map(str, input().split())
if(z == '>'):
    if(int(x) > int(y)):
        print("Right")
    else:
        print("Wrong")
elif(z == '<'):
    if(int(x) < int(y)):
        print("Right")
    else:
        print("Wrong")
elif(z == '='):
    if(int(x) == int(y)):
        print("Right")
    else:
        print("Wrong")