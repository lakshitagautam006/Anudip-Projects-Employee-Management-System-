import psycopg2
from employee import Employee


def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="employee_db",
        user="postgres",
        password="12345",
        port="5432"
    )


def view_employees():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM employees")
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

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        department_id = int(input("Enter Department ID: "))

        query = """
        INSERT INTO employees
        (name, age, gender, phone, email, designation, salary, joining_date, department_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
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

        query = "SELECT * FROM employees WHERE employee_id = %s"

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