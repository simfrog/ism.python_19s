class Employee:
    emp_cnt = 0
    def __init__(self,name='NULL',salary=0):
        self.__name=name
        self.__salary=salary
        Employee.emp_cnt+=1

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_tot_cnt(self):
        return Employee.emp_cnt

name=input("이름:")
salary=int(input("월급:"))
Em=Employee(name,salary)
print(Em.get_name(name))
print(Em.get_salary(salary))
print(Em.get_tot_cnt())

##emplyee.py







