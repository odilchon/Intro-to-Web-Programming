-- Create the staff table
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    position VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    monthly_salary INTEGER NOT NULL,
    start_date DATE NOT NULL
);

-- Insert sample data
INSERT INTO staff (full_name, position, department, monthly_salary, start_date) VALUES
('Michael Scott', 'Manager', 'Sales', 90000, '2018-04-15'),
('Sarah Connor', 'Analyst', 'IT', 72000, '2021-06-10'),
('James Miller', 'Accountant', 'Finance', 65000, '2019-09-01'),
('Olivia Johnson', 'HR Specialist', 'HR', 58000, '2022-02-20'),
('Daniel Carter', 'Developer', 'IT', 85000, '2020-11-05');

-- Retrieve all data
SELECT * FROM staff;

-- Retrieve only names and salaries
SELECT full_name, monthly_salary FROM staff;

-- Retrieve employees in IT department
SELECT * FROM staff
WHERE department = 'IT';
