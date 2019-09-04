class Employee:
    emp_cnt=0
    max_salary=0
    max_name=0
    def __init__(self,name='NULL',salary=0):
        self.name=name
        self.salary=salary
        Employee.emp_cnt+=1
        if int(self.salary)>Employee.max_salary:
            Employee.max_salary=int(self.salary)
            Employee.max_name=self.name
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def get_tot_cnt(self):
        return Employee.emp_cnt
    def get_employee_with_max_salary(self):
        return Employee.max_name

file=open("emp.txt","r")
Employees=list()

for line in file:
    data=line.split()
    emp=Employee(data[0],data[1])
    Employees.append(emp)
# print(Employees)
print(Employees[1].get_employee_with_max_salary())