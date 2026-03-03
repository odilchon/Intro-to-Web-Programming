-- Begin transaction
BEGIN;

-- Insert new customer
INSERT INTO customers (full_name, contact_email, birth_year)
VALUES ('Sophia Martinez', 'sophia@domain.com', 2000);

-- Update existing record
UPDATE customers
SET birth_year = 1999
WHERE contact_email = 'sophia@domain.com';

-- Delete a record
DELETE FROM customers
WHERE full_name = 'Emma Wilson';

-- Rollback changes
ROLLBACK;

-- Verify rollback
SELECT * FROM customers;
