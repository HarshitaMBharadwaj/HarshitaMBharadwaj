#Write a program to calculate the EB Bill.
#The tariff rate for all division is the same. Karnataka electricity board single slaps for the domestic LT supply such as for 0 to 30
#units the per-unit cost will be ? 3.75/-, from 31 to 100 the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ?
#6.75 and above 201 units you have to pay ? 7.8 per unit.
#Additionally, the consumer will pay fixed charges as ? 60/- and electricity tax of 5% extra.

inputis=int(input())
if(inputis>=0 and inputis<=30):
    price=inputis*3.75
elif(inputis>=31 and inputis<=100):
    price=inputis*5.20
elif(inputis>=101 and inputis<=200):
    price=inputis*6.75
elif(inputis>=201):
    price=inputis*7.8
fixedcharge=60
EB=fixedcharge+price
EB=EB+(EB+0.05)
print("EB is :",EB)
