class Employee:
    emp_cnt=0
    def __init__(self,name='NULL',salary=0):
        self.name=name
        self.salary=salary
        Employee.emp_cnt+=1
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def get_tot_cnt(self):
        return Employee.emp_cnt

file=open("emp.txt","r")
Employees=[]
for line in file:
    data=line.split()
    emp = Employee(data[0],data[1])
    Employees.append(emp)
print(Employees)