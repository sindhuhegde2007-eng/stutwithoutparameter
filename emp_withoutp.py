import sys

if len(sys.argv) == 4:
    employee_name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys.argv[3]
    salary = float(sys.argv[4])

else:
    employee_name = "Sindhu"
    employee_id = "1001"
    department = "IT"
    salary = 80000

if salary >= 80000:
    grade = "Grade A"
elif salary >= 60000:
    grade = "Grade B"
elif salary >= 40000:
    grade = "Grade C"
elif salary >= 25000:
    grade = "Grade D"
else:
    grade = "Grade E"

print("Employee Details")
print("----------------")
print("Name       :", employee_name)
print("ID         :", employee_id)
print("Department :", department)
print("Salary     : ₹", salary)
print("Salary Grade:", grade)
