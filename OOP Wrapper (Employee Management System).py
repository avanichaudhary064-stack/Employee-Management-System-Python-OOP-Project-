class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Person Details:")
        print("Name : ",self.name)
        print("Age : ",self.age)

p1 = Person("Avani", 20)
p1.display()


class Employee(Person):
    def __init__(self,name,age,salary,employee_id):
        super().__init__(name, age)  
        self.__salary = salary
        self.__employee_id = employee_id
    def get_employee_id(self):
        return self.__employee_id
    def set_employee_id(self,new_id):
        self.__employee_id = new_id
    def get_salary(self):
        return self.__salary 
    def set_salary(self,new_salary):
        self.__salary = new_salary
    def display(self):
        print("Employee Details:")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.__salary)
        print("Employee ID : ",self.__employee_id)
    def __del__(self):
        print("Employee object deleted.")

e1 = Employee("Avani", 20, 50000, "E101")
e1.display()


class Manager(Employee):
    def __init__(self,name,age,salary,employee_id,department):
        super().__init__(name,age,salary,employee_id)
        self.department = department
    def display(self):
        print("Manager detils")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.get_salary())
        print("Employee ID:", self.get_employee_id())
        print("Department:", self.department)

m1 = Manager("Riya", 35, 80000, "M201", "HR")
m1.display()


class Developer(Employee):
    def __init__(self,name,age,salary,employee_id,programming_language):
        super().__init__(name,age,salary,employee_id)
        self.programming_language = programming_language

    def display(self):
        print("Developer details")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.get_salary())
        print("Employee_ID : ",self.get_employee_id())
        print("Programming Language : ",self.programming_language)

d1 = Developer("Arjun", 28, 60000, "D301", "Python")
d1.display()

print("Inheritance check")
print("Is Manager subclass of Employee?",issubclass(Manager,Employee))
print("Is Developer subclass of Employee?",issubclass(Developer,Employee))

records = []
while True:
    print("---Python OOP Project : Employee Management System---")

    print("Choose an operation:")
    print("1.Create an Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.Show Details")
    print("5.Exit")

    choice = input("Enter your Choice: ")

    if choice == "1":
        name = input("Enter Name : ")
        age = int(input("Enter Age: "))
        p = Person(name, age)
        records.append(p)

    elif choice == "2":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        emp_id = input("Enter Employee ID: ")
        emp = Employee(name, age, salary, emp_id)
        records.append(emp)

    elif choice == "3":
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        emp_id = input("Enter Employee ID: ")
        dept = input("Enter Department: ")
        mgr = Manager(name, age, salary, emp_id,dept)
        records.append(mgr)

    elif choice == "4":
        if len(records) == 0:
            print("No records found.")
        else:
            print("All Records:")
            for obj in records:
                obj.display()

    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Invalid choice! Please try again.")

    