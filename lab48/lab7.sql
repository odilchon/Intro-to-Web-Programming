ALTER TABLE products
ALTER COLUMN price TYPE INTEGER;

-- Verify
SELECT price FROM products;
