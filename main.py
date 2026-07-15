from db import view_employees, add_employee, search_employee

while True:
    print("\n========== Employee Management System ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "6":
        print("Thank you for using Employee Management System!")
        break

    else:
        print("Feature coming soon...")