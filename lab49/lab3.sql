-- Delete customer by email
DELETE FROM customers
WHERE contact_email = 'oliver@domain.com';

-- Delete customers born before 1995
DELETE FROM customers
WHERE birth_year < 1995;

-- Verify
SELECT * FROM customers;
