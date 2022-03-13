#comment
a = input("Enter a=")
b = input("Enter b=")
o = input("Operator")
if o=='+':
    c = int(a) + int(b)
elif o=='-':
    c = int(a) - int(b)
elif o=='*':
    c = int(a) * int(b)
elif o=='/':
    c = int(a) / int(b)
print (" a " + o + " b = ", c)
