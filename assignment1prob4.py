#prob4
a=int(input("enter no 1:"))
b=int(input("enter no 2:"))
c=int(input("enter no 3:"))

max_value=max(a,b,c)
min_value=min(a,b,c)
mid_value=(a+b+c)-(max_value+min_value)

print(max_value,mid_value,min_value,sep='>')
