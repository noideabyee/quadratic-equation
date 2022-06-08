from math import sqrt
a=float(input('enter a: '))
b=float(input('enter b: '))
c=float(input('enter c: '))
delta=(b*b)+((-4)*a*c)
if a==0 and b==0:
    print('IMPOSSIBLE')
elif a==0:
    x=(-c)/b
    print(f"{x*1000//1/1000:.3f}")
elif b==0:
    xBe2=(-c)/a
    jzr=sqrt(xBe2)
    mx=max(jzr,-jzr)
    mn=min(jzr,-jzr)
    print(f"{mn*1000//1/1000:.3f}")
    print(f"{mx*1000//1/1000:.3f}")
elif delta<0:
    print('IMPOSSIBLE')
elif delta>0:
    jzrr=(sqrt(delta))
    x1=((-b)+jzrr)/(2*a)
    x2=((-b)-jzrr)/(2*a)
    mx=max(x1,x2)
    mn=min(x1,x2)
    print(f"{mn*1000//1/1000:.3f}")
    print(f"{mx*1000//1/1000:.3f}")
elif delta==0:
    x1=(-b)/(2*a)
    print(f"{x1*1000//1/1000:.3f}")