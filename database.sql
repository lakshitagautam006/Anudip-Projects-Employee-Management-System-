-- Create Departments Table
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Employees Table
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    designation VARCHAR(100),
    salary DECIMAL(10,2),
    joining_date DATE,
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- Insert Departments
INSERT INTO departments (department_name)
VALUES
('IT'),
('HR'),
('Finance'),
('Marketing'),
('Sales');

-- Insert Sample Employees
INSERT INTO employees
(name, age, gender, phone, email, designation, salary, joining_date, department_id)
VALUES
('Alex Johnson', 25, 'Male', '9876543210', 'alex@example.com',
'Python Developer', 55000, '2026-07-15', 1),

('Sophia Smith', 28, 'Female', '9876543211', 'sophia@example.com',
'HR Executive', 45000, '2025-05-20', 2),

('David Brown', 32, 'Male', '9876543212', 'david@example.com',
'Accountant', 60000, '2024-09-10', 3),

('Emma Wilson', 30, 'Female', '9876543213', 'emma@example.com',
'Marketing Manager', 65000, '2023-03-18', 4),

('James Lee', 27, 'Male', '9876543214', 'james@example.com',
'Sales Executive', 50000, '2025-11-01', 5);