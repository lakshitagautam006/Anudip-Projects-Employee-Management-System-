import psycopg2
import os
from dotenv import load_dotenv
from employee import Employee

load_dotenv()

def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def view_employees():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        query = """
        SELECT
            e.employee_id,
            e.name,
            e.age,
            e.gender,
            e.phone,
            e.email,
            e.designation,
            e.salary,
            e.joining_date,
            d.department_name
        FROM employees e
        JOIN departments d
        ON e.department_id = d.department_id
        """

        cursor.execute(query)
        employees = cursor.fetchall()

        print("\n===== Employee Records =====\n")

        if len(employees) == 0:
            print("No employees found.")

        else:
            for row in employees:
                emp = Employee(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9]
                )

                emp.display()

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

def add_employee():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        print("\n===== Add Employee =====")

        view_departments()

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))
        from datetime import datetime

        joining_date = input("Enter Joining Date (DD-MM-YYYY): ")
        joining_date = datetime.strptime(joining_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        department_id = int(input("Enter Department ID: "))

        query = """
        INSERT INTO employees
        (name, age, gender, phone, email, designation, salary, joining_date, department_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            age,
            gender,
            phone,
            email,
            designation,
            salary,
            joining_date,
            department_id
        )

        cursor.execute(query, values)
        connection.commit()

        print("\nEmployee added successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

def search_employee():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        employee_id = int(input("\nEnter Employee ID: "))

        query = """
        SELECT
            e.employee_id,
            e.name,
            e.age,
            e.gender,
            e.phone,
            e.email,
            e.designation,
            e.salary,
            e.joining_date,
            d.department_name
        FROM employees e
        JOIN departments d
        ON e.department_id = d.department_id
        WHERE e.employee_id = %s
        """

        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()

        if row:
            emp = Employee(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9]
            )

            print("\nEmployee Found:\n")
            emp.display()

        else:
            print("\nEmployee not found!")

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

def update_employee():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        employee_id = int(input("\nEnter Employee ID to update: "))

        # Check if employee exists
        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = %s",
            (employee_id,)
        )

        row = cursor.fetchone()

        if row is None:
            print("\nEmployee not found!")
            cursor.close()
            connection.close()
            return

        print("\n===== Update Employee =====")
        view_departments()

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))
        from datetime import datetime

        joining_date = input("Enter Joining Date (DD-MM-YYYY): ")
        joining_date = datetime.strptime(joining_date, "%d-%m-%Y").strftime("%Y-%m-%d")
        department_id = int(input("Enter Department ID: "))

        query = """
        UPDATE employees
        SET
            name = %s,
            age = %s,
            gender = %s,
            phone = %s,
            email = %s,
            designation = %s,
            salary = %s,
            joining_date = %s,
            department_id = %s
        WHERE employee_id = %s
        """

        values = (
            name,
            age,
            gender,
            phone,
            email,
            designation,
            salary,
            joining_date,
            department_id,
            employee_id
        )

        cursor.execute(query, values)
        connection.commit()

        print("\nEmployee updated successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

def delete_employee():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        employee_id = int(input("\nEnter Employee ID to delete: "))

        # Check if employee exists
        cursor.execute(
            "SELECT * FROM employees WHERE employee_id = %s",
            (employee_id,)
        )

        row = cursor.fetchone()

        if row is None:
            print("\nEmployee not found!")

        else:
            cursor.execute(
                "DELETE FROM employees WHERE employee_id = %s",
                (employee_id,)
            )

            connection.commit()
            print("\nEmployee deleted successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)

def view_departments():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        query = """
        SELECT department_id, department_name
        FROM departments
        ORDER BY department_id
        """

        cursor.execute(query)
        departments = cursor.fetchall()

        print("\nAvailable Departments")
        print("-" * 30)

        for department in departments:
            print(f"{department[0]}. {department[1]}")

        print("-" * 30)

        cursor.close()
        connection.close()

    except Exception as e:
        print("Error:", e)