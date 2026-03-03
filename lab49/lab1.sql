-- Create the customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    contact_email VARCHAR(120) UNIQUE NOT NULL,
    birth_year INTEGER NOT NULL
);

-- Insert records
INSERT INTO customers (full_name, contact_email, birth_year) VALUES
('Michael Brown', 'michael@domain.com', 1998),
('Emma Wilson', 'emma@domain.com', 1995),
('Oliver Taylor', 'oliver@domain.com', 1990);

-- Verify
SELECT * FROM customers;
