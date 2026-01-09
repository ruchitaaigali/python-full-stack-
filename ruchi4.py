name=input("enter the employee name:")
salary=float(input("enter the salary:"))
rating=int(input("enter the performance rating(1-3):"))
if rating==3:
   bonus_percentage=0.20
elif rating==2:
   bonus_percentage=0.15
elif rating==1:
   bonus_percentage=0.10
else:
    bonus_percentage=0.00
bonus_amount=salary*bonus_percentage
final_salary=salary+bonus_amount
print("/n bonus details")
print("employee name:",name)
print("performance rating:",rating)
print("bonus amount:",bonus_amount)
print("final salary:",final_salary)


           
             
           
