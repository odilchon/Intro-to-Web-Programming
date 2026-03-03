-- Create the products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    is_discontinued BOOLEAN DEFAULT FALSE
);

-- Insert product records
INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Smartphone', 800.00),
('Headphones', 150.00);

-- Update the price of a product
UPDATE products
SET price = 1300.00
WHERE name = 'Laptop';

-- Delete discontinued products
DELETE FROM products
WHERE is_discontinued = TRUE;

-- Verify
SELECT * FROM products;
