-- Learn SQL
-- https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
-- Create a new database named "mydb"
CREATE DATABASE mydb;
-- Use the "mydb" database
USE mydb;
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age INT,
    city VARCHAR(255)
);
-- Insert some sample data into the "customers" table
INSERT INTO customers (name, email, age, city) VALUES
('Alice', 'alice@example.com', 30, 'New York'),
('Bob', 'bob@example.com', 25, 'Los Angeles'),
('Charlie', 'charlie@example.com', 35, 'Chicago');
-- Select all records from the "customers" table
SELECT * FROM customers;
-- Select only the "name" and "email" columns from the "customers" table
SELECT name, email FROM customers;
-- Select customers who are older than 30
SELECT * FROM customers WHERE age > 30;
-- Select customers who live in 'New York'
SELECT * FROM customers WHERE city = 'New York';
-- Update the city of a customer
UPDATE customers SET city = 'San Francisco' WHERE name = 'Alice';
-- Delete a customer from the table
DELETE FROM customers WHERE name = 'Bob';
-- Select all records to see the changes
SELECT * FROM customers;
-- Drop the "customers" table
DROP TABLE customers;
-- Drop the "mydb" database
DROP DATABASE mydb;
-- Help me learn JOINS
-- Create two tables: "orders" and "products"
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
-- Insert sample data into "products" table
INSERT INTO products (name, price) VALUES
('Laptop', 999.99),
('Smartphone', 499.99),
('Headphones', 199.99);
-- Insert sample data into "orders" table
INSERT INTO orders (customer_id, product_id, quantity) VALUES
(1, 1, 1), -- Alice orders 1 Laptop
(1, 2, 2), -- Alice orders 2 Smartphones
(2, 3, 1); -- Bob orders 1 Headphones

-- Perform an INNER JOIN to get order details along with product names and prices
-- When to use INNER JOIN: When you want to retrieve only the records that have matching values in both tables. 
-- It returns rows where there is a match in both tables.
SELECT o.id AS order_id, c.name AS customer_name, p.name AS product_name, p.price, o.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN products p ON o.product_id = p.id;

-- Perform a LEFT JOIN to get all customers and their orders (if any)
-- When to use LEFT JOIN: When you want to retrieve all records from the left table (customers) and the matched records from the right table (orders). 
-- It returns all rows from the left table, and the matched rows from the right table. If there is no match, the result is NULL on the right side.
SELECT c.name AS customer_name, p.name AS product_name, o.quantity
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
LEFT JOIN products p ON o.product_id = p.id;

-- Perform a RIGHT JOIN to get all products and the customers who ordered them (if any)
-- When to use RIGHT JOIN: When you want to retrieve all records from the right table (products) and the matched records from the left table (orders). 
-- It returns all rows from the right table, and the matched rows from the left table. If there is no match, the result is NULL on the left side.
SELECT p.name AS product_name, c.name AS customer_name, o.quantity
FROM products p
RIGHT JOIN orders o ON p.id = o.product_id
RIGHT JOIN customers c ON o.customer_id = c.id;

-- Perform a FULL OUTER JOIN to get all customers and products, along with their orders (if any)
-- When to use FULL OUTER JOIN: When you want to retrieve all records when there is a match in either left (customers) or right (products) table. 
-- It returns all rows from both tables, with NULLs in places where the join condition is not met.
SELECT c.name AS customer_name, p.name AS product_name, o.quantity
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id
FULL OUTER JOIN products p ON o.product_id = p.id;

-- Given the table
-- Name     |  Kg  | Date
-- Apple    | 2  | 01/11/2025
-- Orange   | 3  | 05/11/2025
-- Banana   | 10   | 10/11/2025
-- Apple  | 12  | 10/11/2025
-- Banana  | 3  | 15/11/2025
-- Apple  | 10  | 21/11/2025
-- Write a SQL query to find the total weight of each fruit sold in November 2025.
SELECT Name, SUM(Kg) AS Total_Kg
FROM sales
WHERE Date >= '2025-11-01' AND Date <= '2025-11-30'
GROUP BY Name;