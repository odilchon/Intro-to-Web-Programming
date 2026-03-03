-- Employees in IT or Finance
SELECT * FROM staff
WHERE department IN ('IT', 'Finance');

-- Employees with specific salary values
SELECT * FROM staff
WHERE monthly_salary IN (58000, 72000, 90000);
