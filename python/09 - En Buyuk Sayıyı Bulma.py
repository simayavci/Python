a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if a>b and a>c:
    print("{} en büyük sayıdır. ".format(a))
elif b>a and b>c:
    print("{} en büyük sayıdır. ".format(b))
else:
    print("{} en büyük sayıdır. ".format(c))
