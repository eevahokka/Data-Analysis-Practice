-- hr_data_schema.sql
-- This file creates the HR dataset for the SQL + Python project

-- Departments table
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO departments VALUES
(1, 'HR'),
(2, 'Finance'),
(3, 'IT'),
(4, 'Marketing');

-- Employees table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department_id INTEGER,
    hire_date TEXT,
    salary INTEGER
);

INSERT INTO employees VALUES
(1, 'Alice', 1, '2018-06-01', 5000),
(2, 'Bob', 2, '2020-08-12', 6000),
(3, 'Charlie', 3, '2021-01-15', 5500),
(4, 'Diana', 3, '2019-11-23', 7000),
(5, 'Evan', 4, '2022-02-10', 4800),
(6, 'Fay', 1, '2023-03-17', 5100);

-- Salary history
CREATE TABLE salary_history (
    employee_id INTEGER,
    year INTEGER,
    salary INTEGER
);

INSERT INTO salary_history VALUES
(1, 2021, 4200), (1, 2023, 5000),
(2, 2021, 5000), (2, 2023, 6000),
(3, 2021, 4700), (3, 2023, 5500),
(4, 2021, 6300), (4, 2023, 7000),
(5, 2023, 4800),
(6, 2021, 4600);

-- Projects table
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT,
    start_date TEXT
);

INSERT INTO projects VALUES
(1, 'Alpha', '2023-01-01'),
(2, 'Beta', '2023-02-15'),
(3, 'Gamma', '2023-03-01');

-- Timesheets
CREATE TABLE timesheets (
    employee_id INTEGER,
    project_id INTEGER,
    hours INTEGER
);

INSERT INTO timesheets VALUES
(1, 1, 20),
(1, 2, 10),
(2, 1, 25),
(3, 3, 30),
(4, 2, 15),
(5, 3, 10),
(6, 1, 5);

-- Attendance
CREATE TABLE attendance (
    employee_id INTEGER,
    date TEXT,
    status TEXT
);

INSERT INTO attendance VALUES
(1, '2023-07-01', 'Present'),
(1, '2023-07-02', 'Absent'),
(1, '2023-07-03', 'Present'),
(2, '2023-07-01', 'Present'),
(2, '2023-07-02', 'Present'),
(2, '2023-07-03', 'Present'),
(3, '2023-07-01', 'Absent'),
(3, '2023-07-02', 'Absent'),
(3, '2023-07-03', 'Present'),
(4, '2023-07-01', 'Present'),
(4, '2023-07-02', 'Absent'),
(4, '2023-07-03', 'Absent');
