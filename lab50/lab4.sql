-- Salary between 60000 and 80000
SELECT * FROM staff
WHERE monthly_salary BETWEEN 60000 AND 80000;

-- Employees hired between 2019 and 2021
SELECT * FROM staff
WHERE start_date BETWEEN '2019-01-01' AND '2021-12-31';
