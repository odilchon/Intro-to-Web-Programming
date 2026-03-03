ALTER TABLE users
RENAME COLUMN full_name TO name;

-- Verify
SELECT name FROM users;
