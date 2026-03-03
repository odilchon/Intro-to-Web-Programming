-- Transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    branch_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    total_value NUMERIC(12,2) NOT NULL
);

INSERT INTO transactions (branch_id, category_id, total_value) VALUES
(1, 201, 15000),
(1, 202, 25000),
(2, 201, 35000),
(2, 203, 45000),
(3, 204, 110000),
(3, 205, 50000);

-- Purchases table
CREATE TABLE purchases (
    purchase_id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL
);

INSERT INTO purchases (client_id) VALUES
(10), (10), (10), (11), (11), (12), (12), (12), (12),
(13), (13), (14), (14), (14), (14), (14);

-- Staff table
CREATE TABLE team_members (
    member_id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    division_id INTEGER NOT NULL,
    monthly_income INTEGER NOT NULL,
    join_date DATE NOT NULL
);

INSERT INTO team_members (full_name, division_id, monthly_income, join_date) VALUES
('Michael Green', 100, 70000, '2018-06-15'),
('Laura White', 200, 48000, '2020-09-10'),
('Kevin Black', 100, 82000, '2021-02-25'),
('Anna Brown', 300, 53000, '2019-11-30'),
('Tom Harris', 200, 60000, '2022-03-05'),
('Emma Stone', 100, 88000, '2023-01-12');

SELECT branch_id, SUM(total_value) AS branch_total
FROM transactions
GROUP BY branch_id;

SELECT branch_id, SUM(total_value) AS branch_total
FROM transactions
GROUP BY branch_id
HAVING SUM(total_value) > 90000;

SELECT branch_id, category_id, SUM(total_value) AS category_total
FROM transactions
GROUP BY branch_id, category_id;

SELECT client_id, COUNT(purchase_id) AS total_purchases
FROM purchases
GROUP BY client_id;

SELECT division_id, AVG(monthly_income) AS avg_income
FROM team_members
GROUP BY division_id;

SELECT division_id, SUM(monthly_income) AS total_income
FROM team_members
GROUP BY division_id
HAVING SUM(monthly_income) > 150000;

SELECT client_id, COUNT(purchase_id) AS purchase_count
FROM purchases
GROUP BY client_id
HAVING COUNT(purchase_id) > 4;

SELECT MIN(monthly_income) AS lowest_income
FROM team_members;

SELECT MAX(monthly_income) AS highest_income
FROM team_members;
