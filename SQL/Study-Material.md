---

# SQL Study Material

## Table Basics

- **Table**: A table is a collection of related data held in a structured format within a database. It consists of rows and columns, where each row represents a record and each column represents a field or attribute of the record.
- **Column**: A vertical entity in a table that contains all information associated with a specific field.
- **Row**: A horizontal entity in a table that represents a single record or entry, containing data for each column in the table.

## Keys and Constraints

- **Primary Key**: A unique identifier for each record in a table. It ensures that each record can be uniquely identified and prevents duplicate entries.
- **Auto-increment**: A feature that automatically generates a unique number for each new record inserted into a table.
- **Unique Constraint**: Ensures that all values in a column are different from each other, preventing duplicate entries in that column.
- **Foreign Key**: A field in one table that uniquely identifies a row of another table. It establishes a relationship between two tables and enforces referential integrity.
- **Referential Integrity**: A property of data that ensures relationships between tables remain consistent. It means a foreign key in one table must have a corresponding primary key in another table, preventing orphaned records and maintaining data accuracy.

## SQL Joins

- **Join**: An SQL operation that combines rows from two or more tables based on a related column between them. It allows you to retrieve data from multiple tables in a single query, based on the relationships defined by foreign keys.

## Datatypes

- **INT**: Used for whole numbers (e.g., 1, 42, -5).
- **VARCHAR**: Used for variable-length strings (e.g., 'Hello', 'John Doe').
- **DECIMAL**: Used for fixed-point numbers (e.g., 19.99, 100.00).
- **NULL**: Represents a missing or undefined value in a column. Indicates the value is unknown or not applicable.
- **NOT NULL**: A constraint that ensures a column cannot have a NULL value; every record in the column must have a valid value.
- **DEFAULT**: A constraint that provides a default value for a column when no value is specified during record insertion.
- **Datetime**: Used for date and time values (e.g., '2024-06-01 12:00:00').
- **ENUM**: Used for a column that can have one of a predefined set of values (e.g., 'small', 'medium', 'large').
- **BOOLEAN**: Used for true/false values (e.g., TRUE, FALSE).
- **TEXT**: Used for large text data (e.g., articles, descriptions).
- **BLOB**: Used for binary data (e.g., images, files).

This study guide provides a solid foundation for database management. To help you visualize how these concepts translate into actual code, I’ve drafted SQL examples for each section of your material.

---

## 1. Table Basics

A table is structured using the `CREATE TABLE` statement, defining the columns (fields) and their intended data types.

```sql
-- Creating a basic table structure
CREATE TABLE students (
    student_id INT,       -- Column: specific attribute
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- A Row is created when we insert data
INSERT INTO students (student_id, first_name, last_name) 
VALUES (101, 'Jane', 'Doe'); 

```

---

## 2. Keys and Constraints

Constraints ensure your data stays "clean" and accurate. The relationship between a Primary Key and a Foreign Key is the backbone of relational databases.

```sql
-- Table using Primary Key, Auto-increment, and Unique constraints
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier & Auto-gen
    username VARCHAR(30) UNIQUE,            -- Prevents duplicate usernames
    email VARCHAR(100) NOT NULL             -- Ensures field isn't empty
);

-- Table using Foreign Key to establish Referential Integrity
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT, 
    order_date DATETIME,
    -- Links orders to a specific user in the 'users' table
    FOREIGN KEY (user_id) REFERENCES users(user_id) 
);

```

---

## 3. SQL Joins

Joins allow you to pull data from multiple tables as if they were one, provided they share a related column (usually a Foreign Key).

```sql
-- Combining 'users' and 'orders' to see who placed which order
SELECT users.username, orders.order_date
FROM users
JOIN orders ON users.user_id = orders.user_id;

```

---

## 4. Datatypes

Choosing the right datatype optimizes storage and prevents errors (like trying to save "Hello" in a column meant for math).

```sql
CREATE TABLE product_catalog (
    id INT PRIMARY KEY,                     -- Whole numbers
    product_name VARCHAR(255),              -- Variable-length string
    price DECIMAL(10, 2),                   -- Fixed-point (e.g., 19.99)
    description TEXT,                       -- Large text data
    is_available BOOLEAN DEFAULT TRUE,      -- True/False with a Default value
    size ENUM('small', 'medium', 'large'),  -- Predefined set of values
    created_at DATETIME,                    -- Date and time
    product_image BLOB                      -- Binary data (images/files)
);

-- Handling NULL and NOT NULL
INSERT INTO product_catalog (id, product_name, price)
VALUES (1, 'Gaming Mouse', 49.99); 
-- 'description' will be NULL here because no value was provided.

```