-- Update birth year
UPDATE customers
SET birth_year = 1997
WHERE full_name = 'Michael Brown';

-- Update email
UPDATE customers
SET contact_email = 'emma.wilson@domain.com'
WHERE full_name = 'Emma Wilson';

-- Verify
SELECT * FROM customers;
