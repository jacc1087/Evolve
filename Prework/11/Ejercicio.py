import pandas as pd

# Create a dataset of employees
employee_data = {
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"],
    "Salary": [60000, 70000, 80000, 75000, 72000]
}

employee_df = pd.DataFrame(employee_data)

# Calculate average salary by department
department_avg_salary = employee_df.groupby("Department")["Salary"].mean()
print("Average Salary by Department:")
print(department_avg_salary)

# Filter employees with salary above their department's average
employee_df["Above_Avg"] = employee_df.apply(
    lambda row: row["Salary"] > department_avg_salary[row["Department"]], axis= 1)
filtered_employees = employee_df[employee_df["Above_Avg"]]
print("Employees with Salary Above Department Average:")
print(filtered_employees)              