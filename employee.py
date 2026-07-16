from person import Person


class Employee(Person):

    def __init__(
        self,
        employee_id,
        name,
        age,
        gender,
        phone,
        email,
        designation,
        salary,
        joining_date,
        department
    ):
        super().__init__(name, age, gender)

        self.employee_id = employee_id
        self.phone = phone
        self.email = email
        self.designation = designation
        self.salary = salary
        self.joining_date = joining_date
        self.department = department

    def display(self):
         print("-" * 40)
         print(f"Employee ID   : {self.employee_id}")
         print(f"Name          : {self.get_name()}")
         print(f"Age           : {self.get_age()}")
         print(f"Gender        : {self.get_gender()}")
         print(f"Phone         : {self.phone}")
         print(f"Email         : {self.email}")
         print(f"Designation   : {self.designation}")
         print(f"Salary        : ₹{self.salary}")
         print(f"Joining Date  : {self.joining_date}")
         print(f"Department    : {self.department}")
         print("-" * 40)