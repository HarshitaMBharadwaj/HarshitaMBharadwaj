#PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.
#Sample Input 0

#5
#Sample Output 0

#1
 #2
  #3
   #4
    #5

n=int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j==i:
            print(j, end="")
        else:
            print(" ",end="")
    print()
