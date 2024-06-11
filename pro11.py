# #11 #Capital or Small or Digit#
x = input()
if(x >= '0' and x <= '9'):
    print("IS DIGIT")
elif(x >= 'A' and x <= 'Z'):
    print("ALPHA\nIS CAPITAL")
elif(x >= 'a' and x <= 'z'):
    print("ALPHA\nIS SMALL")