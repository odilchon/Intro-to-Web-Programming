CREATE DATABASE my_app_db;

CREATE USER my_app_user WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE my_app_db TO my_app_user;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email) VALUES
('Alice Smith', 'alice@example.com'),
('Bob Jones', 'bob@example.com');

SELECT * FROM users;
