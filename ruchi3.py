course=("python programming","data analytics","AI&ML")
fees=(5000,8000,12000)
discount=(input("enter the discount"))
course_name=(input("enter the course_name"))
fees=int(input("enter the original fees:"))
is_student = True
if is_student:
   print("student discount10%")
   discount_percent=10
else:
    print("early registration discount 5%")
    discount_percent=5
discount_percent=(discount_percent/100)*fees
final_payable=fees-discount_percent
print("final_payable percent:", final_payable)
    
