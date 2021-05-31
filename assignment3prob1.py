#A little girl living in a village craves some rava idli even though she has had rava idli for the last 346514534 days in a row !!
#(Strange, you might think.But its normal down here)
#At the idli shop there are two types of Rava Idli's available.
#One goes for Rs.A per piece and the other goes for Rs.B per piece.
#The girl has a total of K rupees.
#What is the maximum number of rava idlis that she can have?

#Note that she does not care about the type of idli she gets, she just wants to have as many rava idlis of any type as possible.

print("enter the number of test cases")
n=int(input())

for i in range(n):
    print("enter the value of a,b,k")
    a=int(input())
    b=int(input())
    k=int(input())
    if a>=b:
        print(k//b)
    else:
        print(k//a)
