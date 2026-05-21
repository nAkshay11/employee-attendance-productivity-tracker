import pandas as pd

# Load dataset
data = pd.read_csv('employee_productivity_data.csv')

# Productivity efficiency
data['efficiency_score'] = (
    data['tasks_completed'] + data['attendance_days']
) - data['overtime_hours']

# Department-wise productivity
department_productivity = data.groupby('department')['productivity_score'].mean()

# Highest productivity employees
top_employees = data.sort_values(by='productivity_score', ascending=False)

# Average salary
average_salary = data['salary'].mean()

# Print outputs
print("Average Salary:", average_salary)

print("\nDepartment Productivity:")
print(department_productivity)

print("\nTop Employees:")
print(top_employees[['employee_name', 'productivity_score']])

# Save processed file
data.to_csv('processed_employee_data.csv', index=False)

print("\nProcessed employee dataset saved successfully.")