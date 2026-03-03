-- Sort by name A–Z
SELECT * FROM staff
ORDER BY full_name ASC;

-- Sort by salary highest to lowest
SELECT * FROM staff
ORDER BY monthly_salary DESC;

-- Sort by department, then salary
SELECT * FROM staff
ORDER BY department ASC, monthly_salary DESC;
