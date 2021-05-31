#You are given a positive integer . Print a numerical triangle of height  like the one below:

#1
#22
#333
#4444
#55555
#......

number=int(input())
for b in range(0,number):
      y=10**b/9
      print(int(b * y))
