# Miles per Gallon Calaculator
# 10-02-2021
# CTI-110 P2HW1 - Miles Per Gallon
# Jasmine Grimes
#

#1.Enter Miles Driven
miles_driven = float(input('\nEnter miles driven: '))
#2.Enter Gallons Used
gallons_used = float(input('Enter gallons used: '))
#3.Enter Cost Per Gallon
cost_per_gallon = float(input('Enter cost per gallon: '))

mpg = miles_driven / gallons_used
total_gas_cost = cost_per_gallon * gallons_used
cost_per_mile = total_gas_cost / mpg 

print ()
print("Miles Per Gallon ="+format (mpg, ".2f"))
print("Total Gas Cost = $"+format(total_gas_cost,".2f"))
print("Cost Per Mile = $"+format(total_gas_cost / miles_driven,".1f"))

      
