class Employee:
    def __init__(self, employee_id, name, age, gender, phone,
             email, designation, salary, joining_date, department):

        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.designation = designation
        self.salary = salary
        self.joining_date = joining_date
        self.department = department

    def display(self):
        print("-" * 40)
        print(f"Employee ID   : {self.employee_id}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Gender        : {self.gender}")
        print(f"Phone         : {self.phone}")
        print(f"Email         : {self.email}")
        print(f"Designation   : {self.designation}")
        print(f"Salary        : ₹{self.salary}")
        print(f"Joining Date  : {self.joining_date}")
        print(f"Department    : {self.department}")
        print("-" * 40)