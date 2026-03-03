-- Salary greater than 70,000
SELECT * FROM staff
WHERE monthly_salary > 70000;

-- Employees hired after 2020
SELECT * FROM staff
WHERE start_date > '2020-01-01';

-- Employees in Sales or HR
SELECT * FROM staff
WHERE department = 'Sales' OR department = 'HR';
