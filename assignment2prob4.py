#Write a program to calculate the grade. The grade should be calculated in the following method.
#Constraints 
#Score should be in between 1 to 100
#Score
	#>= 90	 --> Grade O
	#>= 80	--> Grade A+
	#>= 70	--> Grade A
	#>= 60	--> Grade B+
	#>= 50	--> Grade B
	#< 50	No Grade

gradein=int(input("enter the marks out of 100:"))

if(1<=gradein<=100):
    
    if(gradein>=90):
        print("Grade O")
        
    elif(gradein>=80):
        print("Grade A+")
        
    elif(gradein>=70):
        print("Grade A")
        
    elif(gradein>=60):
        print("Grade B+")
        
    elif(gradein>=50):
        print("Grade B")
        
    else:
        print("No Grade")
