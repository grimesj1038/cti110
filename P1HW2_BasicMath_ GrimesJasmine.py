Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
    #P1HW2_BasicMath - IDLE Exercise
    # 09-26-2021
    # CTI-110 P1HW2 - Basic Math
    # Grimes, Jasmine
    #
    
nam_Exp = input("Enter name of expense: ")
mon_Charge = input("Enter monthly charge: ")

monthly_tax=float(mon_Charge)*(0.06)
monthly_charge= float(float(monthly_tax) + float(mon_Charge))
annual=float(float(monthly_charge)*12)

print("Bill: "+str(nam_Exp)+" --------- Before Tax: $"+format(float(mon_Charge),".2f"))
print("Monthly Tax: $"+format(monthly_tax,".2f"))
print("Monthly Charge: $"+format(monthly_charge,".2f"))
print("Annual Charge: $"+format(annual,".2f"))



#Enter name of expense or bill.
#then enter the monthly charge of that expense or bill without taxes.
#Program will then give you the monthly & annual charges with a 6% tax
