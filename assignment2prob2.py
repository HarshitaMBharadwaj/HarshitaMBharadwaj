#Read three integers from the keyboard a,b,c, d and those values in the following order.
#max > mid1 > mid2 > min
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=int(input("d="))

list_1=[a,b,c,d]
e=max(list_1)
list_1.remove(e)
f=max(list_1)
list_1.remove(f)
g=max(list_1)
list_1.remove(g)
h=min(list_1)


print(e,f,g,h,sep='>')

