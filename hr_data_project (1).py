# hr_data_project.ipynb (Jupyter Notebook structure)

# ------------------------------
# 📘 Section 1: Introduction
# ------------------------------
"""
This notebook explores a fictional HR dataset using SQL and Python.
We analyze employee tenure, salary growth, departmental structures,
attendance behavior, and project engagement.
All analysis is performed on a shared SQLite database.
"""

# ------------------------------
# 📁 Section 2: Load and Connect to Database
# ------------------------------
import sqlite3

conn = sqlite3.connect("hr_data.db")
cursor = conn.cursor()

# ------------------------------
# 📊 Section 3: SQL Task - Longest Tenure with Current Salary
# ------------------------------
"""
Find the employee with the longest tenure and their current salary.
"""
cursor.execute("""
SELECT e.name, e.hire_date, s.salary
FROM employees e
JOIN salary_history s ON e.id = s.employee_id
WHERE s.year = 2023
ORDER BY e.hire_date ASC
LIMIT 1;
""")
print(cursor.fetchall())

# ------------------------------
# 🐍 Section 4: Python - Employees with >5 Years Tenure
# ------------------------------
from datetime import datetime

def more_than_5y(hire_dates, today):
    counter = 0
    for element in hire_dates:
        year = int(element.split('-')[0])
        this_year = int(today.split('-')[0])
        if this_year - year > 5:
            counter += 1
        elif this_year - year == 5:
            month = int(element.split('-')[1])
            this_month = int(today.split('-')[1])
            if this_month - month > 0:
                counter += 1
            elif this_month - month == 0:
                date = int(element.split('-')[2])
                this_day = int(today.split('-')[2])
                if this_day - date > 0:
                    counter += 1
    return counter

cursor.execute("SELECT hire_date FROM employees")
hire_dates = [row[0] for row in cursor.fetchall()]
print(more_than_5y(hire_dates, "2025-06-10"))

# ------------------------------
# ⏱ Section 5: Project with Most Logged Hours
# ------------------------------
cursor.execute("""
SELECT p.name, SUM(t.hours) as total_hours
FROM projects p
JOIN timesheets t ON p.id = t.project_id
GROUP BY p.name
ORDER BY total_hours DESC
LIMIT 1;
""")
print(cursor.fetchall())

# Python function
hours_dict = {}
cursor.execute("SELECT employee_id, SUM(hours) FROM timesheets GROUP BY employee_id")
for row in cursor.fetchall():
    hours_dict[str(row[0])] = row[1]

def top_employee(dictionary):
    top_e = []
    max_hours = max(dictionary.values())
    for hours in dictionary:
        if max_hours == dictionary[hours]:
            top_e.append(hours)
    return top_e

print(top_employee(hours_dict))

# ------------------------------
# 🏢 Section 6: Employees per Department
# ------------------------------
cursor.execute("""
SELECT d.name, COUNT(e.id) as num_employees
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name
ORDER BY d.name;
""")
print(cursor.fetchall())

# Python function
cursor.execute("SELECT name FROM departments")
departments = [row[0] for row in cursor.fetchall()]

def dictilen(list):
    dic = {}
    for dept in list:
        count = 0
        for char in dept:
            count += 1
        dic[dept] = count
    return dic

print(dictilen(departments))

# ------------------------------
# 💰 Section 7: Salary Growth from 2021 to 2023
# ------------------------------
cursor.execute("""
SELECT e.name, s21.salary AS salary_2021, s23.salary AS salary_2023,
       ROUND(((s23.salary - s21.salary) * 100.0) / s21.salary, 2) AS percent_increase
FROM salary_history s21
JOIN salary_history s23 ON s21.employee_id = s23.employee_id
JOIN employees e ON e.id = s21.employee_id
WHERE s21.year = 2021 AND s23.year = 2023;
""")
print(cursor.fetchall())

cursor.execute("SELECT year, salary FROM salary_history WHERE employee_id = 2")
salaries = cursor.fetchall()

def max_salary(list):
    max_salary = float('-inf')
    year = 0
    for tuple in list:
        if tuple[1] > max_salary:
            max_salary = tuple[1]
            year = tuple[0]
    return year

print(max_salary(salaries))

# ------------------------------
# ✅ Section 8: Attendance Counts per Employee
# ------------------------------
cursor.execute("""
SELECT e.name, COUNT(*)
FROM attendance a
JOIN employees e ON e.id = a.employee_id
WHERE a.status = 'Present'
GROUP BY e.name;
""")
print(cursor.fetchall())

cursor.execute("SELECT e.name, a.date, a.status FROM attendance a JOIN employees e ON a.employee_id = e.id")
attendance_records = cursor.fetchall()

def employee_present(list):
    employees_seen = {}
    for employee in list:
        if employee[2] == "Present":
            if employee[0] not in employees_seen:
                employees_seen[employee[0]] = 1
            else:
                employees_seen[employee[0]] += 1
    return employees_seen

print(employee_present(attendance_records))

# ------------------------------
# 📌 END OF NOTEBOOK
# ------------------------------
"""
This concludes the HR analysis notebook. All data comes from the hr_data.db SQLite database.
Make sure to run the hr_data_schema.sql script to create the database before using this notebook.
"""
